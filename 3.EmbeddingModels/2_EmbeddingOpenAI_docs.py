# MULTI INPUT EMBEDDING

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions = 32)  

documents = [
    "Tanjiro was first to have the demon slayer mark",
    "Tanjiro had the potential of sun breathing hashira.",
    "Demon slayer is a cool anime featuring tanjiro."
]

result = embedding.embed_documents(documents)
print(str(result))