from sentence_transformers import CrossEncoder


class CrossEncoderReranker:
    def __init__(self):
        print("Loading Cross Encoder...")
        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query: str, chunks: list, top_k: int = 3):
        """
        Re-rank retrieved chunks using a Cross Encoder.
        """

        if not chunks:
            return []

        pairs = [
            (query, chunk["text"])
            for chunk in chunks
        ]

        scores = self.model.predict(pairs)

        for chunk, score in zip(chunks, scores):
            chunk["rerank_score"] = float(score)

        reranked = sorted(
            chunks,
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return reranked[:top_k]