from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Morning rain softened the quiet streets",
    "Curiosity often leads minds astray",
    "Old libraries whisper forgotten secrets",
    "Coffee cooled while ideas kept flowing",
    "Night trains carried unfinished conversations"
]

res = embedding.embed_documents(documents)

print(str(res))
