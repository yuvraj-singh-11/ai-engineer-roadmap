from hybrid_search import HybridSearch
from reranker import CrossEncoderReranker
from query_expansion import expand_query
from metadata_filter import filter_results


def print_results(results):

    print("\n" + "=" * 100)
    print("FINAL RANKED RESULTS")
    print("=" * 100)

    for idx, result in enumerate(results, start=1):

        print(f"\nRank #{idx}")
        print(f"Source      : {result['source']}")
        print(f"Chunk ID    : {result['chunk_id']}")

        if "rerank_score" in result:
            print(f"Rerank Score: {result['rerank_score']:.4f}")

        if "rrf_score" in result:
            print(f"RRF Score   : {result['rrf_score']:.6f}")

        print("-" * 100)
        print(result["text"][:400])
        print("-" * 100)


def deduplicate(results):

    unique = {}

    for result in results:

        key = (
            result["source"],
            result["chunk_id"]
        )

        if key not in unique:
            unique[key] = result

    return list(unique.values())


def main():

    print("Initializing Day 15 Advanced Retrieval Pipeline...\n")

    hybrid_search = HybridSearch()
    reranker = CrossEncoderReranker()

    query = input("Ask a legal question: ").strip()

    # --------------------------------------------------
    # Query Expansion
    # --------------------------------------------------

    expanded_queries = expand_query(query)

    print("\nExpanded Queries:")

    for q in expanded_queries:
        print(f"  • {q}")

    # --------------------------------------------------
    # Hybrid Retrieval
    # --------------------------------------------------

    all_results = []

    for expanded_query in expanded_queries:

        results = hybrid_search.search(
            expanded_query,
            k=10
        )

        all_results.extend(results)

    print(
        f"\nRetrieved {len(all_results)} chunks before deduplication"
    )

    # --------------------------------------------------
    # Remove Duplicates
    # --------------------------------------------------

    retrieved_chunks = deduplicate(all_results)

    print(
        f"Retrieved {len(retrieved_chunks)} unique chunks"
    )

    # --------------------------------------------------
    # Metadata Filtering
    # --------------------------------------------------

    # Example:
    # document_type="NDA"

    retrieved_chunks = filter_results(
        retrieved_chunks,
        document_type=None
    )

    print(
        f"After metadata filtering: {len(retrieved_chunks)} chunks"
    )

    # --------------------------------------------------
    # Cross Encoder Re-ranking
    # --------------------------------------------------

    final_results = reranker.rerank(
        query=query,
        chunks=retrieved_chunks,
        top_k=5
    )

    # --------------------------------------------------
    # Output
    # --------------------------------------------------

    print_results(final_results)


if __name__ == "__main__":
    main()