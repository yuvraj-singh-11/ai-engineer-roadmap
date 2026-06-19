# pyrefly: ignore [missing-import]
import chromadb

from legal_docs import documents, ids

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="legal_documents"
)

collection.add(
    documents=documents,
    ids=ids
)

print("Documents stored successfully.")