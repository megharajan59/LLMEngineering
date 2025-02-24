from prompts import prompts
import time
from openai import AzureOpenAI
import pandas as pd
import matplotlib.pyplot as plt
import os
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor

os.environ["AZURE_OPENAI_API_KEY"] = '<your_api_key>'

client = AzureOpenAI(
    azure_endpoint='<your_endpoint>',
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version='<your_api_version>'
)

def measure_latency(prompt):
    start_time = time.time()
    message_text = [{'role':'system','content':prompt['content']}]

    completion = client.chat.completions.create(
        model='gpt-4o',
        messages=message_text,
        temperature=0.7
    )

    print(completion.choices[0].message.content)

    end_time = time.time()

    latency = end_time - start_time

    return latency

latency_values = []
tags = []
prompt_lengths = []

with ThreadPoolExecutor() as executor:
    results = executor.map(measure_latency, prompts)

    for latency, prompt in zip(results, prompts):
        latency_values.append(latency)
        tags.append(prompt['tag'])
        prompt_lengths.append(len(prompt['content'].split()))

print(latency_values)

df = pd.DataFrame({
    "Prompt Type": tags,
    "Prompt Length (words)": prompt_lengths,
    "Latency (seconds)": latency_values,
})

print("\nLatency Table:")
print(df)
headers = ["Prompt Type", "Prompt Length", "Latency"]
table = tabulate(df, headers, tablefmt="grid")
print(table)


plt.figure(figsize=(12, 6))

# 1st Graph: Latency vs Prompt Length (Scatter Plot)
plt.subplot(1, 2, 1)
plt.scatter(df["Prompt Length (words)"], df["Latency (seconds)"], color='blue', label='Latency vs Length')
plt.xlabel("Prompt Length (words)")
plt.ylabel("Latency (seconds)")
plt.title("Latency vs Prompt Length")


# 2nd Graph: Latency vs Prompt Type (Bar Chart)
plt.subplot(1, 2, 2)
plt.barh(df["Prompt Type"], df["Latency (seconds)"], color='blue', label='Latency vs Prompt Types')
plt.xlabel("Latency (seconds)")
plt.title("Latency vs Prompt Type")


plt.tight_layout()
plt.show()
