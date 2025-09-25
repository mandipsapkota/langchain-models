from langchain_openai import OpenAI
from dotenv import load_dotenv
# load from env 
load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

result = llm.invoke("Who is the coolest anime characte ever?")

print(result)