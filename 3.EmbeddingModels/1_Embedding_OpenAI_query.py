from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions = 32)  
# 1536 to 30724 is limit of dimensions ranging from small to large vectors


# SINGLE QUERY EMBEDDING
result = embedding.embed_query("Tanjiro is a potential sun breathing Hashira.")

print(str(result))