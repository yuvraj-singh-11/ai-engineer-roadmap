from chroma_store import collection

def search_documents(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    formatted_results = []

    for i in range(len(results["ids"][0])):
        formatted_results.append(
            {
                "id": results["ids"][0][i],
                "title": results["metadatas"][0][i]["title"],
                "document": results["documents"][0][i],
                "distance": results["distances"][0][i]
            }
        )

    return formatted_results