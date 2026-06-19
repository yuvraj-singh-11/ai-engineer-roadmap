# Legal Document Semantic Search API

A mini Legal AI project built using FastAPI, Sentence Transformers, and ChromaDB.

This project demonstrates how modern Legal AI systems perform semantic search using embeddings instead of traditional keyword matching.

---

## Features

- Legal document dataset
- Sentence embeddings using Sentence Transformers
- ChromaDB vector database
- Semantic search API
- FastAPI Swagger documentation
- Persistent vector storage

---

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- ChromaDB
- Uvicorn

---

## Project Structure

```text
mini-project/
│
├── data/
│
├── app.py
├── documents.py
├── embedder.py
├── chroma_store.py
├── search.py
│
├── requirements.txt
├── README.md
│
└── chroma_db/
```

---

## Architecture

```text
Legal Documents
        │
        ▼
Sentence Transformers
        │
        ▼
Embeddings
        │
        ▼
ChromaDB
        │
        ▼
Semantic Search
        │
        ▼
FastAPI Endpoint
```

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd mini-project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn app:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Legal Semantic Search API"
}
```

---

### Semantic Search

```http
GET /search?query=termination clause
```

Example Response:

```json
{
  "query": "termination clause",
  "results": [
    {
      "id": "2",
      "title": "Vendor Agreement",
      "document": "The agreement may be terminated with thirty days written notice.",
      "distance": 0.23
    }
  ]
}
```

---

## Sample Queries

### Contract Termination

```text
termination clause
```

Expected Result:

```text
Vendor Agreement
```

---

### Employment Benefits

```text
employee salary
```

Expected Result:

```text
Employment Agreement
```

---

### Confidentiality

```text
confidential information
```

Expected Result:

```text
NDA Agreement
```

---

### Privacy Compliance

```text
privacy regulations
```

Expected Result:

```text
Data Privacy Policy
```

---

## What I Learned

### FastAPI

- API development
- Route creation
- Query parameters
- Swagger documentation

### Embeddings

- Text to vector conversion
- Semantic understanding
- Similarity search

### ChromaDB

- Vector database fundamentals
- Document storage
- Semantic retrieval

### Legal AI Concepts

- Embeddings
- Vector Search
- Semantic Search
- Retrieval Systems
- RAG Foundations

---

## Future Improvements

- PDF document ingestion
- Document chunking
- OpenAI integration
- Retrieval-Augmented Generation (RAG)
- Multi-document search
- Metadata filtering
- LangChain integration
- LangGraph workflows

---

## Author

Yuvraj Singh

AI Engineer Roadmap – Week 1 Mini Project
