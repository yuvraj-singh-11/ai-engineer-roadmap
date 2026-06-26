from bm25_search import BM25Search
from vector_search import VectorSearch

class HybridSearch:
    def __init__(self):
        self.bm25_searcher = BM25Search()
        self.vector_searcher = VectorSearch()

    def search(self, query: str, k: int = 5):
        """
        Merge results using Reciprocal Rank Fusion (RRF).
        RRF Score = 1 / (k + rank)
        """
        # Fetch more candidates initially to get a good intersection
        fetch_k = max(k * 2, 20)
        
        bm25_results = self.bm25_searcher.search(query, k=fetch_k)
        vector_results = self.vector_searcher.search(query, k=fetch_k)

        rrf_scores = {}
        chunks_map = {}

        # The RRF constant (usually 60 in literature, but can be tweaked)
        RRF_K = 60

        def add_to_rrf(results, weight=1.0):
            for rank, r in enumerate(results, start=1):
                chunk_key = (r["source"], r["chunk_id"])
                
                if chunk_key not in rrf_scores:
                    rrf_scores[chunk_key] = 0.0
                    chunks_map[chunk_key] = r
                
                rrf_scores[chunk_key] += weight * (1.0 / (RRF_K + rank))

        add_to_rrf(bm25_results, weight=1.0)
        add_to_rrf(vector_results, weight=1.0)

        # Sort by RRF score descending
        sorted_chunks = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

        # Return top k
        final_results = []
        for chunk_key, score in sorted_chunks[:k]:
            chunk_data = chunks_map[chunk_key]
            chunk_data["rrf_score"] = round(score, 6)
            final_results.append(chunk_data)

        return final_results

if __name__ == "__main__":
    searcher = HybridSearch()
    results = searcher.search("termination clause", k=5)
    for r in results:
        print(f"[{r['source']}:{r['chunk_id']}] RRF Score: {r['rrf_score']}")
