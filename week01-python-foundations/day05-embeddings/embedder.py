# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer
from legal_docs import documents

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)

print("\nDocuments:")
for doc in documents:
    print("-", doc)

print("\nEmbedding Shape:")
print(embeddings.shape)

print("\nFirst 10 values of first embedding:")
print(embeddings[0][:10])
