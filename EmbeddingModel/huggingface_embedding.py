from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

texts = [
    "hello, how are you?",
    "wish you doing best"
]

vector = embedding.embed_documents(texts)
print(vector)