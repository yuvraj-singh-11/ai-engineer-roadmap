from chroma_store import collection
from embedder import get_embeddings

def retrieve(query, top_k=5):
    query_embedding = get_embeddings([query])[0]
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    return results["documents"][0]
