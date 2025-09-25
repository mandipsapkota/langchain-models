from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model = "gpt-4o-mini",temperature=1.8,max_completion_tokens = 10)

result = chat_model.invoke("who would win between a all out battle on yoorichi and demon king tanjiro")

print(result)