from query import LegalRetriever
from evaluator import RAGEvaluator
from test_questions import TEST_QUESTIONS


def run_evaluation(k: int = 3):
    retriever = LegalRetriever()
    evaluator = RAGEvaluator()

    all_results = []

    print(f"\n🚀 Running RAG evaluation with k={k}\n")

    for idx, item in enumerate(TEST_QUESTIONS, 1):
        question = item["question"]
        expected_sources = item["expected_sources"]
        expected_keywords = item["expected_keywords"]

        retrieved = retriever.retrieve_diverse(question, k=k, initial_k=30)
        metrics = evaluator.evaluate_one(
            expected_sources=expected_sources,
            expected_keywords=expected_keywords,
            retrieved_chunks=retrieved,
            k=k
        )

        result = {
            "question_no": idx,
            "question": question,
            "expected_sources": expected_sources,
            "retrieved": retrieved,
            "metrics": metrics
        }
        all_results.append(result)

        print(f"Q{idx}: {question}")
        print(f"Expected Sources: {expected_sources}")
        print(f"Retrieved Sources: {metrics['retrieved_sources']}")
        print(
            f"Metrics -> Hit@{k}: {metrics['hit_at_k']}, "
            f"Source Recall@{k}: {metrics['source_recall_at_k']}, "
            f"Source Precision@{k}: {metrics['source_precision_at_k']}, "
            f"Keyword Coverage: {metrics['keyword_coverage']}"
        )

        if metrics["missing_expected_sources"]:
            print(f"Missing Expected Sources: {metrics['missing_expected_sources']}")

        print("Top chunks:")
        for rank, chunk in enumerate(retrieved, 1):
            print(
                f"  {rank}. {chunk['source']} | chunk_id={chunk['chunk_id']} | score={chunk['score']}"
            )
        print("-" * 80)

    summary = evaluator.summarize(all_results)

    print("\n📊 Overall Summary")
    print(f"Average Hit@{k}: {summary['avg_hit_at_k']}")
    print(f"Average Source Recall@{k}: {summary['avg_source_recall_at_k']}")
    print(f"Average Source Precision@{k}: {summary['avg_source_precision_at_k']}")
    print(f"Average Keyword Coverage: {summary['avg_keyword_coverage']}\n")


if __name__ == "__main__":
    run_evaluation(k=3)