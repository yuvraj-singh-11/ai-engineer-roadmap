class RAGEvaluator:
    @staticmethod
    def evaluate_one(expected_sources, expected_keywords, retrieved_chunks, k):
        topk = retrieved_chunks[:k]
        retrieved_sources = [c["source"] for c in topk]

        expected_set = set(expected_sources)
        retrieved_set = set(retrieved_sources)

        covered_expected = expected_set.intersection(retrieved_set)

        # Better for multi-source questions
        source_recall_at_k = len(covered_expected) / len(expected_set) if expected_set else 0.0
        source_precision_at_k = len(covered_expected) / len(retrieved_set) if retrieved_set else 0.0

        # old binary hit (still useful)
        hit_at_k = 1 if len(covered_expected) > 0 else 0

        context = " ".join([c["text"].lower() for c in topk])
        matched_keywords = [kw for kw in expected_keywords if kw.lower() in context]
        keyword_coverage = len(matched_keywords) / len(expected_keywords) if expected_keywords else 0.0

        return {
            "hit_at_k": hit_at_k,
            "source_recall_at_k": round(source_recall_at_k, 4),
            "source_precision_at_k": round(source_precision_at_k, 4),
            "keyword_coverage": round(keyword_coverage, 4),
            "matched_keywords": matched_keywords,
            "retrieved_sources": retrieved_sources,
            "covered_expected_sources": sorted(list(covered_expected)),
            "missing_expected_sources": sorted(list(expected_set - retrieved_set)),
        }

    @staticmethod
    def summarize(all_results):
        n = len(all_results)
        if n == 0:
            return {
                "avg_hit_at_k": 0.0,
                "avg_source_recall_at_k": 0.0,
                "avg_source_precision_at_k": 0.0,
                "avg_keyword_coverage": 0.0,
            }

        return {
            "avg_hit_at_k": round(sum(r["metrics"]["hit_at_k"] for r in all_results) / n, 4),
            "avg_source_recall_at_k": round(sum(r["metrics"]["source_recall_at_k"] for r in all_results) / n, 4),
            "avg_source_precision_at_k": round(sum(r["metrics"]["source_precision_at_k"] for r in all_results) / n, 4),
            "avg_keyword_coverage": round(sum(r["metrics"]["keyword_coverage"] for r in all_results) / n, 4),
        }