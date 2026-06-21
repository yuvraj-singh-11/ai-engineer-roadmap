# day07-rag-basics/chroma_store.py
import chromadb
from chromadb.utils import embedding_functions
from documents import KNOWLEDGE_BASE

def get_vector_collection():
    # Initialize a local persistent client
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    
    # Use a built-in, free, local embedding function (Sentence Transformers)
    # This downloads a small model    locally on first run automatically
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Get or create collection
    collection = chroma_client.get_or_create_collection(
        name="company_knowledge", 
        embedding_function=emb_fn
    )
    
    # Populate collection if empty
    if collection.count() == 0:
        ids = [doc["id"] for doc in KNOWLEDGE_BASE]
        documents = [doc["text"] for doc in KNOWLEDGE_BASE]
        collection.add(ids=ids, documents=documents)
        print(f"--> Successfully indexed {len(documents)} documents into ChromaDB.")
        
    return collection

if __name__ == "__main__":
    # Test initialization
    coll = get_vector_collection()
    print(f"Collection count: {coll.count()}")
