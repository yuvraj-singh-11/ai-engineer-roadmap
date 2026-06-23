# query.py

import chromadb
from chromadb.utils import embedding_functions

DB_DIR = "chroma_db"
COLLECTION_NAME = "legal_documents"


class LegalRetriever:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=DB_DIR
        )

        self.embedding_function = (
            embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="all-MiniLM-L6-v2"
            )
        )

        self.collection = self.client.get_collection(
            name=COLLECTION_NAME,
            embedding_function=self.embedding_function
        )

    def retrieve_context(
        self,
        query,
        top_k=5
    ):

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = "\n\n".join(documents)

        return context, documents, metadatas