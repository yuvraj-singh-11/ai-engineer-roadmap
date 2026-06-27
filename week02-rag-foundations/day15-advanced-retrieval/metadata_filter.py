def filter_results(results, document_type=None):
    if not document_type:
        return results

    filtered = []

    for result in results:
        metadata = result.get("metadata", {})

        if metadata.get("document_type") == document_type:
            filtered.append(result)

    return filtered