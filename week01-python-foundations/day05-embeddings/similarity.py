# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from legal_docs import documents

model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embeddings = model.encode(documents)

query = "Confidentiality Agreement"

query_embedding = model.encode([query])

similarities = cosine_similarity(
query_embedding,
doc_embeddings
)

print(f"\nQuery: {query}\n")

for index, score in enumerate(similarities[0]):
    print(
f"Document: {documents[index]}"
)
print(
f"Similarity Score: {score:.4f}"
)
print("-" * 50)

best_match_index = similarities.argmax()

print("\nBest Match:")
print(documents[best_match_index])

print(
f"Score: {similarities[0][best_match_index]:.4f}"
)
