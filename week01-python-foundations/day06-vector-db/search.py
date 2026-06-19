# pyrefly: ignore [missing-import]
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="legal_documents"
)

query = "Confidentiality Agreement"

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("Query:")
print(query)

print("\nResults:")

for doc in results["documents"][0]:
    print(doc)