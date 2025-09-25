from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Anime is cool",
    "Drawing is cool",
    "Guitar is cool",
    "Coding is cool",
    "Robots are cool",
    "I am cool"
]

vector = embedding.embed_documents(documents)

print(str(vector))