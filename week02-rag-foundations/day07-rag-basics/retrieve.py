# day07-rag-basics/retrieve.py
from chroma_store import get_vector_collection

def retrieve_context(query: str, n_results: int = 1):
    collection = get_vector_collection()
    
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    retrieved_chunks = results['documents'][0] if results['documents'] else []
    return retrieved_chunks