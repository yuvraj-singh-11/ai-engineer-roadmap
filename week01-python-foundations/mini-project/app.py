from fastapi import FastAPI
from documents import LEGAL_DOCUMENTS
from chroma_store import collection
from search import search_documents

app = FastAPI()

# Load documents only if they don't already exist
existing_ids = collection.get()["ids"]

for doc in LEGAL_DOCUMENTS:
    if str(doc["id"]) not in existing_ids:
        collection.add(
            ids=[str(doc["id"])],
            documents=[doc["content"]],
            metadatas=[
                {
                    "title": doc["title"]
                }
            ]
        )

@app.get("/")
def home():
    return {
        "message": "Legal Semantic Search API"
    }

@app.get("/search")
def search(query: str):
    results = search_documents(query)

    return {
        "query": query,
        "results": results
    }