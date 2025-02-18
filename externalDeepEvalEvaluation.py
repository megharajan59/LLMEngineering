import openai
import os
from langfuse.decorators import langfuse_context, observe
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams, LLMTestCase
import math
from langfuse import Langfuse
from datetime import datetime, timedelta

os.environ["LANGFUSE_PUBLIC_KEY"] = "<your_public_key>"
os.environ["LANGFUSE_SECRET_KEY"] = "<your_secret_key>"
os.environ["LANGFUSE_HOST"] = "http://localhost:3000"
os.environ["OPENAI_API_KEY"] = "<your_api_key>"

BATCH_SIZE = 10
TOTAL_TRACES = 50

langfuse = Langfuse(
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    host="http://localhost:3000"
)

now = datetime.now()
five_am_today = datetime(now.year, now.month, now.day, 5, 0)
five_am_yesterday = five_am_today - timedelta(days=1)

# template for helpfulness matrix in Langfuse 
helpfulness_template = """
Evaluate the helpfulness of the generation on a continuous scale from 0 to 1. 
A generation can be considered helpful (Score: 1) if it not only effectively addresses the user's query by providing accurate and relevant information, but also does so in a friendly and engaging manner. 
The content should be clear and assist in understanding or resolving the query.

Example:
Query: Can eating carrots improve your vision?
Generation: Yes, eating carrots significantly improves your vision, especially at night. 
This is why people who eat lots of carrots never need glasses. Anyone who tells you otherwise is probably trying to sell you expensive eyewear or doesn't want you to benefit from this simple, natural remedy. 
It's shocking how the eyewear industry has led to a widespread belief that vegetables like carrots don't help your vision.
People are so gullible to fall for these money-making schemes.
Score: 0.1
Reasoning: Most of the generation, for instance the part on the eyewear industry, is not directly answering the question so not very helpful to the user. 
Furthermore, disrespectful words such as ‘gullible’ make the generation unfactual and thus, unhelpful. 
Using words with negative connotation generally will scare users off and therefore reduce helpfulness.

Query: What are some beginner-friendly programming languages?
Generation: Python is one of the easiest programming languages for beginners because of its simple syntax. 
JavaScript is also a good option if you want to build websites. However, some people think C++ is better, but it’s much harder to learn.
Score: 0.7
Reasoning: The response provides useful recommendations (Python and JavaScript) but is somewhat biased against C++. 
It would be more helpful if it objectively explained the strengths and weaknesses of each language instead of dismissing C++ outright.

Query: What’s the best way to prepare for a job interview?
Generation: Research the company and role, practice answering common interview questions, and prepare a few questions to ask the interviewer. 
Also, dress professionally and make sure to arrive on time.
Score: 0.8
Reasoning: The response gives practical, concise advice but could be improved by including additional tips, such as mock interviews, understanding company culture, or improving body language.

Query: How does inflation affect the economy?
Generation: Inflation decreases the purchasing power of money, meaning goods and services become more expensive over time. 
Moderate inflation is normal and even beneficial for economic growth, but high inflation can reduce consumer spending and create economic instability. Central banks often adjust interest rates to control inflation.
Score: 0.9
Reasoning: The response is clear, accurate, and informative, covering both positive and negative aspects of inflation. It could be slightly improved by including real-world examples or historical references.

Query: What are some healthy breakfast options?
Generation: You should just eat whatever you like. Some people eat junk food, and they seem fine. Who cares about breakfast, anyway?
Score: 0.0
Reasoning: The response is dismissive, lacks useful information, and contradicts the intent of the query. It neither provides healthy breakfast options nor encourages a balanced diet.

Query: How does photosynthesis work?
Generation: Photosynthesis is a process where plants use sunlight to produce food. 
It involves light energy being converted into chemical energy through reactions in the chloroplasts. 
The main components are carbon dioxide, water, and sunlight, which produce glucose and oxygen.
Score: 1.0
Reasoning: The response is concise, scientifically accurate, and clearly structured.
It answers the query effectively without unnecessary details or confusion.


Input:
Query: {{query}}
Generation: {{generation}}

Think step by step.
"""

def helpfulness_score(trace):
    helpfulness_metric = GEval(
        name="Helpfulness",
        criteria="Determine whether the output was helpful with respect to the context and query.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
    )
    test_case = LLMTestCase(
        input=trace.input["args"],
        actual_output=trace.output)

    helpfulness_metric.measure(test_case)

    print(f"Score: {helpfulness_metric.score}")
    print(f"Reason: {helpfulness_metric.reason}")

    return {"score": helpfulness_metric.score, "reason": helpfulness_metric.reason}

def tone_score(trace):
    return openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": helpfulness_template.format(text=trace.output),
            }
        ],
        model="gpt-4o",
        temperature=0
    ).choices[0].message.content


for page_number in range(1, math.ceil(TOTAL_TRACES / BATCH_SIZE)):

    # fetch the trace project for historical traces
    traces_batch = langfuse.fetch_traces(
        tags="ext_eval_pipelines",
        page=page_number,
        from_timestamp=five_am_yesterday,
        to_timestamp=datetime.now(),
        limit=BATCH_SIZE
    ).data

    for trace in traces_batch:
        print(f"Processing {trace.name}")

        if trace.output is None:
            print(f"Warning: \n Trace {trace.name} had no generated output, \
            it was skipped")
            continue

        langfuse.score(
            trace_id=trace.id,
            name="helpfulness_tone",
            value=tone_score(trace)
        )

        hscore = helpfulness_score(trace)
        langfuse.score(
            trace_id=trace.id,
            name="helpfulness",
            value=hscore["score"],
            comment=hscore["reason"]
        )

    print(f"Batch {page_number} processed 🚀 \n")
