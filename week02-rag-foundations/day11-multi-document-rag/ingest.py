# day11-multi-document-rag/ingest.py

import os
import chromadb
from chromadb.utils import embedding_functions

DOCS_DIR = "documents"
DB_DIR = "chroma_db"
COLLECTION_NAME = "legal_documents"


def chunk_text(text, chunk_size=200, overlap=50):
    """
    Split text into overlapping chunks.
    """
    words = text.split()

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])

        if chunk.strip():
            chunks.append(chunk)

    return chunks


def initialize_ingestion():
    print("=" * 60)
    print("🚀 INITIALIZING MULTI-DOCUMENT INGESTION PIPELINE")
    print("=" * 60)

    # Verify folder exists
    if not os.path.exists(DOCS_DIR):
        print(f"❌ Error: '{DOCS_DIR}' directory not found.")
        return

    # Find all txt files
    files = [
        f for f in os.listdir(DOCS_DIR)
        if f.endswith(".txt")
    ]

    print(f"📂 Found {len(files)} TXT files")

    if not files:
        print("⚠️ No TXT files found.")
        return

    # Initialize Chroma
    chroma_client = chromadb.PersistentClient(path=DB_DIR)

    # Delete old collection during development
    try:
        chroma_client.delete_collection(COLLECTION_NAME)
        print("🗑️ Old collection deleted")
    except Exception:
        pass

    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    collection = chroma_client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=emb_fn
    )

    total_chunks = 0

    for file_name in files:

        file_path = os.path.join(DOCS_DIR, file_name)

        print(f"\n⚙️ Processing: {file_name}")

        try:
            # Read text file
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            if not text.strip():
                print(f"   ⚠️ Skipping empty file: {file_name}")
                continue

            # Chunk document
            chunks = chunk_text(
                text=text,
                chunk_size=200,
                overlap=50
            )

            print(f"   📄 Created {len(chunks)} chunks")

            ids = []
            documents = []
            metadatas = []

            for i, chunk in enumerate(chunks):

                ids.append(
                    f"{file_name}_chunk_{i}"
                )

                documents.append(chunk)

                metadatas.append(
                    {
                        "source": file_name,
                        "chunk_id": i
                    }
                )

            collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )

            total_chunks += len(chunks)

            print(
                f"   ✅ Stored {len(chunks)} chunks in ChromaDB"
            )

        except Exception as e:
            print(
                f"   ❌ Failed to process {file_name}: {str(e)}"
            )

    print("\n" + "=" * 60)
    print("🎉 INGESTION COMPLETE")
    print("=" * 60)

    print(f"📁 Documents Processed : {len(files)}")
    print(f"📦 Total Chunks       : {total_chunks}")
    print(f"🗄️ Collection Count   : {collection.count()}")

    print("\n📚 Sources Stored:")

    for file_name in files:
        print(f"   • {file_name}")

    print("\n✅ Multi-document knowledge base ready.")


if __name__ == "__main__":
    initialize_ingestion()