import os
import json
import chromadb

from sentence_transformers import SentenceTransformer
# pyrefly: ignore [missing-import]
from langchain_text_splitters import RecursiveCharacterTextSplitter


DATA_FOLDER = "data"
COLLECTION_NAME = "legal_documents"


class LegalDocumentIngestor:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

        self.embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )

    def load_documents(self):

        documents = []

        for file_name in os.listdir(DATA_FOLDER):

            if file_name.endswith(".txt"):

                file_path = os.path.join(
                    DATA_FOLDER,
                    file_name
                )

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

                documents.append(
                    {
                        "source": file_name,
                        "text": text
                    }
                )

        return documents

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            split_chunks = self.text_splitter.split_text(
                document["text"]
            )

            for chunk_id, chunk_text in enumerate(split_chunks):

                chunks.append(
                    {
                        "text": chunk_text,
                        "source": document["source"],
                        "chunk_id": chunk_id
                    }
                )

        return chunks

    def store_chunks(self, chunks):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.embedding_model.encode(
            texts,
            show_progress_bar=True
        ).tolist()

        ids = [
            f"{chunk['source']}_{chunk['chunk_id']}"
            for chunk in chunks
        ]

        metadatas = [
            {
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"]
            }
            for chunk in chunks
        ]

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )

        print(
            f"\n✅ Stored {len(chunks)} chunks in ChromaDB"
        )
        
        # Save chunks to json so bm25_search can load it without chroma
        with open("chunks.json", "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=4)
            
        print(f"✅ Saved chunks to chunks.json for BM25 retrieval.")

    def run(self):

        print("Loading documents...")

        documents = self.load_documents()

        print(f"Loaded {len(documents)} documents")

        chunks = self.chunk_documents(documents)

        print(f"Created {len(chunks)} chunks")

        self.store_chunks(chunks)


if __name__ == "__main__":

    ingestor = LegalDocumentIngestor()

    ingestor.run()
