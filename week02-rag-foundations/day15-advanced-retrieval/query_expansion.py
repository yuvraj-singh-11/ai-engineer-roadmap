def expand_query(query: str):
    expansions = {
        "termination": [
            "contract termination",
            "termination clause",
            "cancellation provision",
            "exit clause",
        ],
        "liability": [
            "legal responsibility",
            "indemnification",
            "damages",
        ],
        "confidentiality": [
            "confidential information",
            "non-disclosure",
            "nda obligations",
        ],
    }

    expanded_queries = [query]

    for keyword, related_queries in expansions.items():
        if keyword in query.lower():
            expanded_queries.extend(related_queries)

    return list(set(expanded_queries))