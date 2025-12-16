import os
from openai import OpenAI

client = OpenAI(
    api_key='sk-e24ff97440d941e48b4a5cacc3d67253',
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Tell me a joke"},
    ],
    stream=False
)

print(response.choices[0].message.content)
