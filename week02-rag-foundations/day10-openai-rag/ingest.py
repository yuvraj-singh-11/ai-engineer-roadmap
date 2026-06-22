import os
import chromadb
from sentence_transformers import SentenceTransformer

def chunk_text(text, chunk_size=50, overlap=10):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def main():
    print("Document Loaded")
    with open("data/nda.pdf", "r", encoding="utf-8") as f:
        text = f.read()
    
    print("Chunks Created")
    chunks = chunk_text(text, chunk_size=50, overlap=10)
    
    print("Embeddings Generated")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(chunks).tolist()
    
    print("Stored in ChromaDB")
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="legal_documents")
    
    # Optional: clear existing data before re-inserting to prevent duplicates during testing
    # if collection.count() > 0:
    #     client.delete_collection("legal_documents")
    #     collection = client.get_or_create_collection(name="legal_documents")
        
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        metadatas=[{"source": "nda.pdf", "chunk_id": i} for i in range(len(chunks))]
    )
    print("Ingestion Complete!")

if __name__ == "__main__":
    main()