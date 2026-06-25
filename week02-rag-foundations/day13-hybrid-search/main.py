from bm25_search import BM25Search
from vector_search import VectorSearch
from hybrid_search import HybridSearch


def run_queries():
    queries = [
        "termination clause",
        "confidential information",
        "indemnification",
        "governing law",
        "liability limitation"
    ]

    print("Initializing Searchers...")
    bm25 = BM25Search()
    vector = VectorSearch()
    hybrid = HybridSearch()
    
    k = 3

    for q in queries:
        print("\n" + "="*60)
        print(f"🔍 QUERY: '{q}'")
        print("="*60)

        print("\n--- BM25 ONLY ---")
        res_bm25 = bm25.search(q, k=k)
        for i, r in enumerate(res_bm25, 1):
            print(f" {i}. [{r['source']}:{r['chunk_id']}] Score: {r['score']}")

        print("\n--- VECTOR ONLY ---")
        res_vec = vector.search(q, k=k)
        for i, r in enumerate(res_vec, 1):
            print(f" {i}. [{r['source']}:{r['chunk_id']}] Score: {r['score']}")

        print("\n--- HYBRID (RRF) ---")
        res_hyb = hybrid.search(q, k=k)
        for i, r in enumerate(res_hyb, 1):
            print(f" {i}. [{r['source']}:{r['chunk_id']}] RRF: {r['rrf_score']}")

if __name__ == "__main__":
    run_queries()
