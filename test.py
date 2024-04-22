import openai
import requests
import os
from openai import OpenAI

os.environ["HTTP_PROXY"] = "http://localhost:7890"
os.environ["HTTPS_PROXY"] = "http://localhost:7890"

api_key = "sk-C6n3jndE0SV8fKVJ4aF2F8A225B54c2b901c966a16765bCb"
base_url = "https://lonlie.plus7.plus/v1"

import openai

openai.api_key = 'your-api-key-here'

# 列表中包含多个问题
questions = [
    "What is the capital of France?",
    "What is the capital of Italy?",
    "What is the capital of Germany?"
]

messages = [{"role": "system", "content": "You are a helpful assistant."}]
for question in questions:
    messages.append({"role": "user", "content": question})
    messages.append({"role": "user", "content": "continue"})

# 调用ChatCompletion API

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.chat.completions.create(
    messages=messages,
    model="gpt-3.5-turbo",
    max_tokens=1024,
    temperature=0.7,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=2,
    stop=["\n\n", "\n16", "16.", "16 ."],
    logprobs=True,
    n=2,    
)

print(response)