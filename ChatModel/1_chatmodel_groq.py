from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile",temperature=0.9,max_tokens=20)
result = model.invoke("whrite a paragraph on machine")
print(result.content)