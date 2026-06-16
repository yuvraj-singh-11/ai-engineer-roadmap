from pydantic import BaseModel


class LegalDocument(BaseModel):
    id: int
    title: str
    document_type: str
    risk_level: str
    