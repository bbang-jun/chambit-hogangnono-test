import bardapi
import os
import config

bard_api_key = config.bard_api_key

# api key를 입력하세요.
os.environ['_BARD_API_KEY']=bard_api_key

# 질문작성
input_text = "현재 한국 대통령이 누구야?"

# 바드 대답
response = bardapi.core.Bard().get_answer(input_text)
print(response['content'])