from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
              model="gemini-embedding-001",
              dimensions=768
              )
texts  = [
      "hello,how are you?",
      "wish you doing best"
]
vector = embeddings.embed_documents(texts)
print(vector)
