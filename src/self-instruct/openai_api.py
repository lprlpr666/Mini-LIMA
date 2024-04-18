import json
import tqdm
import os
import random
import openai
from datetime import datetime
import argparse
import time
    
# both make_requests and make_chat_requests are used to make requests to OpenAI API
# make_requests is used for completions API
# make_chat_requests is used for chat.conlpetions API
# prompts: list of prompts
# response: "text" is the response text

#example output for main:
# Prompt: Write a tagline for an ice cream shop.
# Response: "Scoops of happiness in every cone."

def make_requests(
        prompts, max_tokens, temperature, top_p, 
        frequency_penalty, presence_penalty, stop_sequences, logprobs, n, best_of, retries=3, api_key=None, base_url=None, organization=None, model="gpt-3.5-turbo-instruct"
    ):
    response = None
    target_length = max_tokens
    if api_key is not None:
        openai.api_key = api_key
    if base_url is not None:
        openai.base_url = base_url
    if organization is not None:
        openai.organization = organization
    retry_cnt = 0
    backoff_time = 30
    while retry_cnt <= retries:
        try:            
            response = openai.OpenAI(api_key=api_key, base_url=base_url).completions.create(
                model=model,
                prompt=prompts,
                max_tokens=target_length,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop_sequences,
                # logprobs=logprobs,
                n=n,
                best_of=best_of,
            )
            break
        except openai.APIError as e:
            print(f"OpenAIError: {e}.")
            if "Please reduce your prompt" in str(e):
                target_length = int(target_length * 0.8)
                print(f"Reducing target length to {target_length}, retrying...")
            else:
                print(f"Retrying in {backoff_time} seconds...")
                time.sleep(backoff_time)
                backoff_time *= 1.5
            retry_cnt += 1
    
    if isinstance(prompts, list):
        results = []
        for j, prompt in enumerate(prompts):
            data = {
                "prompt": prompt,
                "response": {"choices": response.choices[j * n: (j + 1) * n]} if response else None,
                "text": response.choices[j * n].text if response.choices else "",
                "created_at": str(datetime.now()),
            }
            results.append(data)
        return results
    else:
        data = {
            "prompt": prompts,
            "response": response,
            "created_at": str(datetime.now()),
        }
        return [data]
    
def make_chat_requests(
        prompts, max_tokens, temperature, top_p,
        frequency_penalty, presence_penalty, stop_sequences, logprobs, n, best_of, retries=3, api_key=None, base_url=None, organization=None, model="gpt-3.5-turbo"
):
    response = None
    if api_key is not None:
        openai.api_key = api_key
    if base_url is not None:
        openai.base_url = base_url
    if organization is not None:
        openai.organization = organization
    data = []
    for prompt in prompts:
        retry_cnt = 0
        backoff_time = 30
        while retry_cnt <= retries:
            try:
                response = openai.OpenAI(api_key=api_key, base_url=base_url).chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},                    
                        {"role": "user", "content": prompt},                        
                    ],
                    model=model,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    frequency_penalty=frequency_penalty,
                    presence_penalty=presence_penalty,
                    stop=stop_sequences,
                    logprobs=logprobs,
                    n=n,
                )
                data.append({
                    "prompt": prompt,
                    "response": {"choices": response.choices} if response else None,
                    "text": response.choices[0].message.content if response.choices else "",
                    "created_at": str(datetime.now()),
                })
                break
            except openai.APIError as e:
                print(f"OpenAIError: {e}.")
                print(f"Retrying in {backoff_time} seconds...")
                time.sleep(backoff_time)
                backoff_time *= 1.5
                retry_cnt += 1
    return data    

    
if __name__ == "__main__":
    prompts = [
        "Write a tagline for an ice cream shop.",
        "What is the capital of France?",
        "What is the capital of Italy?",
    ]
    response = make_requests(
        prompts=prompts,
        max_tokens=1024,
        temperature=0.7,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=2,
        stop_sequences=["\n16", "16.", "16 ."],
        logprobs=False,
        n=1,
        best_of=1,
        api_key="sk-C6n3jndE0SV8fKVJ4aF2F8A225B54c2b901c966a16765bCb",
        base_url="https://lonlie.plus7.plus/v1",
    )
    
    for i, res in enumerate(response):
        print(f"Prompt: {prompts[i]}\nResponse: {res['text']}\n")