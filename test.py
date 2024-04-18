import openai
import requests
import os
from openai import OpenAI

os.environ["HTTP_PROXY"] = "http://localhost:7890"
os.environ["HTTPS_PROXY"] = "http://localhost:7890"

api_key = "sk-C6n3jndE0SV8fKVJ4aF2F8A225B54c2b901c966a16765bCb"
base_url = "https://lonlie.plus7.plus/v1"

client = OpenAI(api_key=api_key, base_url=base_url)
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ],
    model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    stop=["\n\n", "\n16", "16.", "16 ."],
    logprobs=False,
    n=1,    
)
print(chat_completion)