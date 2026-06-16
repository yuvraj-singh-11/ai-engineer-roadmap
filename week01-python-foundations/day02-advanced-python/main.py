from legal_document import LegalDocument
from document_manager import DocumentManager


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():

    print("===== LEGAL DOCUMENT MANAGEMENT SYSTEM =====")

    manager = DocumentManager()

    # Read contract file
    contract_content = read_file("data/sample_contract.txt")

    contract = LegalDocument(
        document_id=1,
        title="Employment Agreement",
        document_type="Contract",
        content=contract_content
    )

    # Read NDA file
    nda_content = read_file("data/sample_nda.txt")

    nda = LegalDocument(
        document_id=2,
        title="Vendor NDA",
        document_type="NDA",
        content=nda_content
    )

    # Add documents
    manager.add_document(contract)
    manager.add_document(nda)

    # List documents
    print("\nListing Documents:")
    manager.list_documents()

    # Search document
    print("\nSearching for 'NDA':")

    results = manager.search_document("NDA")

    if results:
        for document in results:
            document.display()
    else:
        print("No document found.")

    # Count document types
    print("\nDocument Count By Type:")

    counts = manager.count_documents_by_type()

    for doc_type, count in counts.items():
        print(f"{doc_type}: {count}")

    # Save documents
    manager.save_to_json("data/documents.json")

    # Load documents
    manager.load_from_json("data/documents.json")


if __name__ == "__main__":
    main()