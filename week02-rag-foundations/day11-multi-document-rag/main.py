# main.py

from query import LegalRetriever
from generator import generate_answer


def print_sources(metadatas):
    print("\n📚 Sources Used")

    seen = set()

    for meta in metadatas:
        source = meta["source"]

        if source not in seen:
            print(f"   • {source}")
            seen.add(source)


def main():

    print("=" * 60)
    print("⚖️ LEGAL MULTI-DOCUMENT RAG")
    print("=" * 60)

    retriever = LegalRetriever()

    while True:

        question = input(
            "\nAsk a legal question (or type 'exit'): "
        ).strip()

        if question.lower() == "exit":
            print("\n👋 Exiting Legal RAG")
            break

        try:
            # Step 1: Retrieve relevant chunks
            context, documents, metadatas = (
                retriever.retrieve_context(
                    question,
                    top_k=5
                )
            )

            # Step 2: Generate answer using Groq
            answer = generate_answer(
                question,
                context
            )

            # Step 3: Show final answer
            print("\n" + "=" * 60)
            print("🤖 GENERATED ANSWER")
            print("=" * 60)

            print(answer)

            # Step 4: Show retrieved chunks
            print("\n" + "=" * 60)
            print("📄 RETRIEVED CHUNKS")
            print("=" * 60)

            for idx, (doc, meta) in enumerate(
                zip(documents, metadatas),
                start=1
            ):

                print(
                    f"\n[{idx}] Source: {meta['source']}"
                )

                print(
                    f"Chunk ID: {meta['chunk_id']}"
                )

                print("-" * 40)

                preview = (
                    doc[:400] + "..."
                    if len(doc) > 400
                    else doc
                )

                print(preview)

            # Step 5: Show source documents
            print_sources(metadatas)

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()