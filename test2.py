from openai import OpenAI
from os import getenv

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

questions = [
    "What is the capital of France?",
    "What is the capital of Italy?",
    "What is the capital of Germany?"
]

messages = [{"role": "system", "content": "You are a helpful assistant."}]
for question in questions:
    messages.append({"role": "user", "content": question})
    messages.append({"role": "user", "content": "continue"})

completion = client.completions.create(
    model="mistralai/mistral-7b-instruct:free",
    prompt=[
        "What is the capital of France?",
        "What is the capital of Italy?",
    ],
    top_p=1,
    temperature=0.85,
    frequency_penalty=0.34,
    presence_penalty=0.06,
)
print(completion.choices[0].message.content)