import chromadb
from sentence_transformers import SentenceTransformer


COLLECTION_NAME = "legal_documents"


class VectorSearch:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)
        self.embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def search(self, question: str, k: int = 5):
        query_embedding = self.embedding_model.encode(question).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            include=["documents", "metadatas", "distances"]
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        distances = results["distances"][0]

        retrieved = []
        for doc, meta, dist in zip(docs, metas, distances):
            # Chroma returns distance (lower is better).
            # Convert to a simple score where higher is better.
            score = 1 / (1 + dist)

            retrieved.append(
                {
                    "text": doc,
                    "source": meta.get("source"),
                    "chunk_id": meta.get("chunk_id"),
                    "score": round(score, 6),
                    "distance": dist
                }
            )

        return retrieved

if __name__ == "__main__":
    searcher = VectorSearch()
    results = searcher.search("termination clause", k=3)
    for r in results:
        print(f"[{r['source']}:{r['chunk_id']}] Score: {r['score']}")
