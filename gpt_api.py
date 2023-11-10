import os
import openai
import config
openai.api_key = config.gpt_api_key

messages = []

while True:
    user_contents = input("user : ") # 사용자 입력 받기
    messages.append({"role" : "user", "content" : f"{user_contents}"}) # 사용자의 입력을 user라는 role로 메세지로 추가

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages) # message를 넣고 gpt 실행

    gpt_contents = completion.choices[0].message["content"].strip()
    messages.append({"role" : "assistant", "content" : f"{gpt_contents}"})

    print(f"abcedfGPT : {gpt_contents}") # gpt의 결과 출력
    print()