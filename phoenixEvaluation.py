import openai
import os
from langfuse.decorators import langfuse_context, observe
from langfuse import Langfuse
import pandas as pd
from phoenix.evals import OpenAIModel, HallucinationEvaluator,QAEvaluator,run_evals

from uuid import uuid4

os.environ["LANGFUSE_PUBLIC_KEY"] = "<your_public_key>"
os.environ["LANGFUSE_SECRET_KEY"] = "<your_secret_key>"
os.environ["LANGFUSE_HOST"] = "http://localhost:3000"
os.environ["OPENAI_API_KEY"] = "<your_api_key>"

langfuse = Langfuse(
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    host="http://localhost:3000"
)


def generate_output(question):

    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        model="gpt-4o",

        temperature=1
    ).choices[0].message.content
    print(f"Answer: {response}")

    return response

def evaluate_and_log(question, answer):
    """Evaluates hallucination & QA correctness and logs results to Langfuse."""
    eval_model = OpenAIModel(model="gpt-4o", api_key="<your_api_key>")
    hallucination_evaluator = HallucinationEvaluator(eval_model)
    qa_correctness_evaluator = QAEvaluator(eval_model)

    df = pd.DataFrame({
        "input": [question],
        "reference": ["You are a helpful assistant. Provide the most accurate response to the user's question."],
        "output": [answer],
    })

    hallucination_eval_df, qa_correctness_eval_df = run_evals(
        dataframe=df,
        evaluators=[hallucination_evaluator, qa_correctness_evaluator],
        provide_explanation=True,
    )

    # Extracting scores and explanations
    hallucination_score = float(hallucination_eval_df.score.iloc[0])
    hallucination_reason = str(hallucination_eval_df.explanation.iloc[0])

    qa_score = float(qa_correctness_eval_df.score.iloc[0])
    qa_reason = str(qa_correctness_eval_df.explanation.iloc[0])

    print(langfuse_context.get_current_trace_id())

    # Log to Langfuse
    langfuse.score(name="hallucination", value=hallucination_score, comment=hallucination_reason)
    langfuse.score(name="qa_correctness", value=qa_score, comment=qa_reason)

    print(f"Hallucination Score: {hallucination_score}, Reason: {hallucination_reason}")
    print(f"QA Correctness Score: {qa_score}, Reason: {qa_reason}")

if __name__ == "__main__":

    print("\n**Interactive AI Chat & Evaluation**")
    print("Type your questions below (or type 'exit' to quit).")

    while True:
        question = input("\nAsk me anything: ").strip()

        if question.lower() == "exit":
            print("\n**Exiting... Thanks for using the AI Chat!**")
            break

        # Create the trace in Langfuse
        trace = langfuse.trace(
            name=f"trace_for_{question}",
            tags=[f"new_phoenix_eval_{question}"]
        )

        # Generate output and evaluate
        answer = generate_output(question)
        evaluate_and_log(question, answer)
