import json
from legal_document import LegalDocument


class DocumentManager:

    def __init__(self):
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)
        print(f"Document '{document.title}' added successfully.")

    def remove_document(self, document_id):
        for document in self.documents:
            if document.document_id == document_id:
                self.documents.remove(document)
                print("Document removed successfully.")
                return

        print("Document not found.")

    def list_documents(self):
        if not self.documents:
            print("No documents available.")
            return

        print("\n===== DOCUMENT LIST =====")

        for document in self.documents:
            document.display()

    def search_document(self, keyword):
        found_documents = []

        for document in self.documents:

            if (
                keyword.lower() in document.title.lower()
                or keyword.lower() in document.document_type.lower()
            ):
                found_documents.append(document)

        return found_documents

    def count_documents_by_type(self):
        document_count = {}

        for document in self.documents:

            doc_type = document.document_type

            if doc_type in document_count:
                document_count[doc_type] += 1
            else:
                document_count[doc_type] = 1

        return document_count

    def save_to_json(self, file_path):

        try:

            data = []

            for document in self.documents:
                data.append(document.to_dict())

            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)

            print("Documents saved successfully.")

        except Exception as e:
            print(f"Error saving documents: {e}")

    def load_from_json(self, file_path):

        try:

            with open(file_path, "r") as file:
                data = json.load(file)

            self.documents = []

            for item in data:

                document = LegalDocument(
                    document_id=item["document_id"],
                    title=item["title"],
                    document_type=item["document_type"],
                    content=item["content"]
                )

                self.documents.append(document)

            print("Documents loaded successfully.")

        except FileNotFoundError:
            print("JSON file not found.")

        except Exception as e:
            print(f"Error loading documents: {e}")