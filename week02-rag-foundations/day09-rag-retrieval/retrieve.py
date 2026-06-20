from embedder import get_embeddings
from chroma_store import collection

def retrieve(query, k=1):

    query_embedding = get_embeddings(
        [query]
    )[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]