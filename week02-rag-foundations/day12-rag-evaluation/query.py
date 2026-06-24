import chromadb
from sentence_transformers import SentenceTransformer


COLLECTION_NAME = "legal_documents"


class LegalRetriever:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)
        self.embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def retrieve(self, question: str, k: int = 3):
        """
        Input:
            question (str), k (int)
        Output:
            List[dict] with:
            - text
            - source
            - chunk_id
            - score (similarity proxy from distance)
        """
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

    def retrieve_diverse(self, question: str, k: int = 5, initial_k: int = 20):
        """
        Two-stage retrieval:
        1) Fetch top `initial_k` by similarity
        2) Re-rank to improve source diversity (at most one chunk/source first),
           then fill remaining slots by score.
        Returns: List[dict] with text, source, chunk_id, score, distance
        """
        query_embedding = self.embedding_model.encode(question).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=initial_k,
            include=["documents", "metadatas", "distances"]
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        dists = results["distances"][0]

        candidates = []
        for doc, meta, dist in zip(docs, metas, dists):
            candidates.append({
                "text": doc,
                "source": meta.get("source"),
                "chunk_id": meta.get("chunk_id"),
                "distance": dist,
                "score": round(1 / (1 + dist), 6),  # higher is better
            })

        # Stage 2A: pick best chunk per source first (diversity pass)
        selected, seen_sources = [], set()
        for c in candidates:
            if c["source"] not in seen_sources and len(selected) < k:
                selected.append(c)
                seen_sources.add(c["source"])

        # Stage 2B: fill remaining by global relevance
        if len(selected) < k:
            used = {(x["source"], x["chunk_id"]) for x in selected}
            for c in candidates:
                key = (c["source"], c["chunk_id"])
                if key not in used:
                    selected.append(c)
                    used.add(key)
                if len(selected) >= k:
                    break

        return selected[:k]


if __name__ == "__main__":
    retriever = LegalRetriever()
    question = "Which agreements contain termination clauses?"
    
    print("--- Standard Retrieve (k=10) ---")
    results_std = retriever.retrieve(question, k=10)
    for i, r in enumerate(results_std, 1):
        print(f"Rank {i} | Source: {r['source']} | Score: {r['score']}")
        
    print("\n--- Diverse Retrieve (k=10, initial_k=30) ---")
    results_div = retriever.retrieve_diverse(question, k=10, initial_k=30)
    for i, r in enumerate(results_div, 1):
        print(f"Rank {i} | Source: {r['source']} | Score: {r['score']}")