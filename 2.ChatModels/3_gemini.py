from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-pro")

output = model.invoke("Why dont we have circular laptops?")

print(output.content)