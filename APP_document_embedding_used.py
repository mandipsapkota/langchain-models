from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions = 300)

documents = [
    "Tanjiro Kamado is the main protagonist who uses Water and Sun Breathing.",
    "Nezuko Kamado is Tanjiro’s sister who was turned into a demon and uses a Blood Demon Art.",
    "Zenitsu Agatsuma is a Thunder Breathing user who shows bravery when unconscious.",
    "Inosuke Hashibira is a wild and hot-headed Beast Breathing user.",
    "Kyojuro Rengoku is the Flame Hashira who is passionate and honorable."
]

document_embeddings = embedding.embed_documents(documents) # 5 vector set

while True:
    query = input('Enter your query:')
    if query == "exit":
        break
    else:
        query_embeddings = embedding.embed_query(query) # query vector
        scores = cosine_similarity([query_embeddings],document_embeddings)[0] # both values should be a list, and using [0] because we got a 2d list.

        index,score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]

        print(f"Query : {query}")
        print(f"Answer : {documents[index]}")
        print(f"Similarity score : {score}")
        print("Type exit to exit.")

print("Thank you for using the app.")