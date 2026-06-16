from fastapi import FastAPI
from data import documents
from models import LegalDocument


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Yuvraj's AI Engineer Roadmap API"
    }


@app.get("/documents")
def get_documents():
    return documents


@app.get("/documents/{document_id}")
def get_document(document_id: int):

    for doc in documents:

        if doc["id"] == document_id:   
            return doc

    return {
        "error": "Document not found"
    }


@app.post("/documents")
def add_document(document: LegalDocument):
    documents.append(document.model_dump())
    return document


@app.delete("/documents/{document_id}")
def delete_document(document_id: int):
    for doc in documents:
        if doc["id"] == document_id:
            documents.remove(doc)
            return {
                "message": "Document deleted successfully"
            }
    return {
        "error": "Document not found"
    }

@app.patch("/documents/{id}")
def update_document(id: int, updated_document: LegalDocument):
    for doc in documents:
        if doc["id"] == id:
            doc.update(updated_document.model_dump())
            return doc
    return {
        "error": "Document not found"
    }
@app.get("/documents/risk/{risk_level}")
def get_document_by_risk_level(risk_level: str):
    for doc in documents:
        if doc["risk_level"].lower() == risk_level.lower():
            return doc
    return {
        "error": "Document not found"
    }