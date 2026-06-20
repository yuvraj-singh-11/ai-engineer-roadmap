from loader import load_document
from chunker import chunk_text
from embedder import get_embeddings
from chroma_store import collection
from retrieve import retrieve

document = load_document(
    "contracts/master_service_agreement.txt"
)

chunks = chunk_text(
    document,
    chunk_size=500,
    overlap=150
)

collection.add(
    ids=[str(i) for i in range(len(chunks))],
    documents=chunks,
    embeddings=get_embeddings(chunks)
)

query = input(
    "Ask a question: "
)

results = retrieve(query)

for chunk in results:
    print("\n")
    print(chunk)