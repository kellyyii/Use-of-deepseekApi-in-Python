import os
from openai import OpenAI
import time

key='sk-e24ff97440d941e48b4a5cacc3d67253'
api_url="https://api.deepseek.com"

def printChar(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def sendToDeepseek(ans):
    print("Authenticating, Please wait...")
    client = OpenAI(api_key=key, base_url=api_url)
    print("Loading...")
    
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": ans},
    ],
    stream=False
) 
    return response.choices[0].message.content

while True:
    myinput = input("Please say: ")
    res = sendToDeepseek(myinput)
    printChar(res)
    
    print('---------------------------------------')

