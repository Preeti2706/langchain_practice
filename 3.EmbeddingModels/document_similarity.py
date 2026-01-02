from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Rohit Sharma led India under match pressure",
    "India openers built pressure through aggressive match starts",
    "Virat Kohli handled match pressure during India chases",
    "Bumrah delivered under pressure securing India victories",
    "India fielding sustained pressure to close matches"
]

query = 'Tell me about Virat Kohli'

doc_emb = embedding.embed_documents(documents)
query_emb = embedding.embed_query(query)

scores = cosine_similarity([query_emb], doc_emb)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(documents[index])
print("similarity score is: ", score)

