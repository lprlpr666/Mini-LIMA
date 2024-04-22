from openai import OpenAI
from os import getenv

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENROUTER_API_KEY"),
)

completion = client.completions.create(
    extra_headers={
    },
    model="mistralai/mistral-7b-instruct:free",
    prompt=[
        {"role": "user", "content": "What is your favourite condiment?"},
        {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!"},
        {"role": "user", "content": "Do you have mayonnaise recipes?"}
    ],
    top_p=1,
    temperature=0.85,
    frequency_penalty=0.34,
    presence_penalty=0.06,
)
print(completion.choices[0].message.content)