from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import sys
sys.stdout.reconfigure(encoding='utf-8')
load_dotenv() 
model = ChatMistralAI(model="mistral-small-2506",temperature=1,max_tokens=20)
result = model.invoke("what is my name")
print(result.content)