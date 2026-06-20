from loader import load_document
from chunker import chunk_text

FILE_PATH = "contracts/vendor_agreement.txt"

document = load_document(FILE_PATH)

print("=" * 50)
print("DOCUMENT LENGTH")
print("=" * 50)

print(len(document))

chunks = chunk_text(
    document,
    chunk_size=500,
    overlap=100
)

print("\n")
print("=" * 50)
print("TOTAL CHUNKS")
print("=" * 50)

print(len(chunks))

for index, chunk in enumerate(chunks, start=1):

    print("\n")
    print("=" * 50)
    print(f"CHUNK {index}")
    print("=" * 50)

    print(chunk)