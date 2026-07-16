from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv() 
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash",temperature=1,max_tokens=20)
result = model.invoke("what is the capital of india")
print(result.content)