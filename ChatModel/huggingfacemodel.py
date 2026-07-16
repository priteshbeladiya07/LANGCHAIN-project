from dotenv import load_dotenv
load_dotenv()
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ.get("HUGGINGFACEHUB_ACCESS_TOKEN", "")
os.environ["HF_TOKEN"] = os.environ.get("HUGGINGFACEHUB_ACCESS_TOKEN", "")

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model = ChatHuggingFace(llm = llm)
response = model.invoke("how are you ?")
print(response.content)