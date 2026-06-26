from hybrid_search import HybridSearch
from reranker import CrossEncoderReranker


QUERIES = [
    "termination clause",
    "confidential information",
    "indemnification",
    "governing law",
    "liability limitation"
]


def print_hybrid_results(results):
    print("\n--- HYBRID RESULTS ---")

    for i, r in enumerate(results, start=1):
        print(
            f"{i}. "
            f"[{r['source']}:{r['chunk_id']}] "
            f"RRF: {r['rrf_score']}"
        )


def print_reranked_results(results):
    print("\n--- CROSS ENCODER RERANKED ---")

    for i, r in enumerate(results, start=1):
        print(
            f"{i}. "
            f"[{r['source']}:{r['chunk_id']}] "
            f"Score: {r['rerank_score']:.4f}"
        )


def main():

    print("Initializing Hybrid Search...")
    hybrid = HybridSearch()

    print("Initializing Cross Encoder...")
    reranker = CrossEncoderReranker()

    for query in QUERIES:

        print("\n" + "=" * 60)
        print(f"QUERY: '{query}'")
        print("=" * 60)

        # Retrieve top 10 candidates
        hybrid_results = hybrid.search(
            query,
            k=10
        )

        print_hybrid_results(hybrid_results)

        # Re-rank and keep best 3
        reranked = reranker.rerank(
            query=query,
            chunks=hybrid_results,
            top_k=3
        )

        print_reranked_results(reranked)


if __name__ == "__main__":
    main()