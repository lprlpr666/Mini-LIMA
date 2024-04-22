import openai
import requests
import os
from openai import OpenAI

os.environ["HTTP_PROXY"] = "http://localhost:7890"
os.environ["HTTPS_PROXY"] = "http://localhost:7890"

api_key = "sk-C6n3jndE0SV8fKVJ4aF2F8A225B54c2b901c966a16765bCb"
base_url = "https://lonlie.plus7.plus/v1"

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.completions.create(
    prompt=[
        "Write a tagline for an ice cream shop.",
        "What is the capital of France?",
        "What is the capital of Italy?",
    ],
    model="gpt-3.5-turbo-instruct",
    max_tokens=1024,
    temperature=0.7,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=2,
    stop=["\n16", "16.", "16 ."],
    # # logprobs=1,
    n=1,    
    best_of=1,
)

print(response)