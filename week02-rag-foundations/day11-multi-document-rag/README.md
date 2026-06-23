# Day 11 - Multi-Document RAG System

## Objective

Build a production-style Multi-Document Retrieval-Augmented Generation (RAG) system capable of:

* Ingesting multiple legal documents
* Generating embeddings
* Storing vectors in ChromaDB
* Retrieving relevant chunks using semantic search
* Generating answers using an LLM (Groq)
* Providing source attribution for transparency

---

# Project Architecture

```text
User Question
      │
      ▼
Embedding Model
(all-MiniLM-L6-v2)
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Similarity Search
(Top-K Retrieval)
      │
      ▼
Relevant Chunks
      │
      ▼
Context Construction
      │
      ▼
Groq LLM
(Llama 3.3)
      │
      ▼
Generated Answer
      │
      ▼
Source Attribution
```

---

# Documents Used

The system was trained on three legal documents:

```text
documents/

├── nda.txt
├── employment.txt
└── msa.txt
```

### NDA

Contains:

* Confidentiality clauses
* Intellectual Property clauses
* Governing law
* Dispute resolution
* Termination provisions

### Employment Agreement

Contains:

* Salary
* Notice period
* Confidentiality obligations
* Employee IP ownership
* Termination conditions

### Master Services Agreement (MSA)

Contains:

* Service obligations
* SLA commitments
* Security requirements
* Confidentiality clauses
* Termination and liability clauses

---

# Components Implemented

## 1. Multi-Document Ingestion

Implemented:

```python
ingest.py
```

Responsibilities:

* Load all legal documents
* Chunk text into smaller sections
* Generate embeddings
* Store chunks in ChromaDB

---

## 2. Chunking Strategy

Implemented fixed-size chunking:

```python
chunk_size = 200
overlap = 50
```

Purpose:

* Improve retrieval accuracy
* Preserve context across chunk boundaries
* Reduce information loss

---

## 3. Embedding Generation

Model Used:

```text
all-MiniLM-L6-v2
```

Characteristics:

* 384-dimensional embeddings
* Lightweight
* Fast inference
* Good semantic retrieval performance

---

## 4. ChromaDB Integration

Vector database:

```text
ChromaDB
```

Collection:

```text
legal_documents
```

Stored:

* Document chunks
* Embeddings
* Metadata

Example Metadata:

```json
{
  "source": "employment.txt",
  "chunk_id": 15
}
```

---

## 5. Semantic Retrieval

Implemented:

```python
query.py
```

Workflow:

1. User asks a question
2. Question converted into embedding
3. ChromaDB performs similarity search
4. Top-K chunks returned

Example:

```text
Question:
What is the notice period for resignation?

Retrieved:
employment.txt
Chunk 21
Chunk 22
Chunk 23
```

---

## 6. Context Construction

Retrieved chunks are combined into a single context:

```python
context = "\n\n".join(documents)
```

This context is passed to the LLM.

---

## 7. LLM Integration

Implemented:

```python
generator.py
```

Model:

```text
Llama-3.3-70B-Versatile
```

Provider:

```text
Groq
```

Prompt Strategy:

* Answer only from provided context
* Avoid hallucinations
* Return fallback response when information is unavailable

---

## 8. Source Attribution

Every answer includes source information.

Example:

```text
Sources:

• nda.txt
• employment.txt
```

Benefits:

* Transparency
* Trust
* Legal traceability
* Easier debugging

---

# Sample Queries Tested

### NDA Questions

```text
What is the confidentiality period?

Who owns intellectual property?

What is the governing law?
```

### Employment Questions

```text
What is the notice period for resignation?

What happens during probation?

What are the employee obligations?
```

### MSA Questions

```text
What are the SLA penalties?

What security requirements exist?

What are the payment terms?
```

### Cross-Document Questions

```text
Which agreements contain termination clauses?

Which documents mention intellectual property?

Which agreements contain confidentiality obligations?
```

---

# Key Concepts Learned

## Multi-Document RAG

Single Document RAG:

```text
Question
 ↓
One Document
 ↓
Answer
```

Multi-Document RAG:

```text
Question
 ↓
Multiple Documents
 ↓
Retriever
 ↓
Top-K Chunks
 ↓
LLM
 ↓
Answer
```

---

## Metadata

Metadata enables source tracking.

Example:

```json
{
  "source": "nda.txt",
  "chunk_id": 34
}
```

Without metadata:

```text
Answer found
```

With metadata:

```text
Answer found in:
nda.txt
Chunk 34
```

---

## Retrieval Quality

The quality of a RAG system depends heavily on:

* Chunking strategy
* Embedding quality
* Retrieval accuracy
* Top-K selection

Poor retrieval leads to poor answers.

---

# Challenges Faced

### Issue 1

Attempted to parse text files as PDFs.

Error:

```text
invalid pdf header
EOF marker not found
```

Resolution:

* Identified documents were plain text files
* Switched ingestion logic to text processing

---

### Issue 2

Initially stored one document as one vector.

Problem:

```text
Large documents
↓
Poor retrieval quality
```

Resolution:

Implemented chunking.

---

### Issue 3

Source tracking.

Resolution:

Added metadata for every chunk.

---

# Final Outcome

Successfully built:

✅ Multi-Document Ingestion

✅ Chunking Pipeline

✅ Embedding Generation

✅ ChromaDB Storage

✅ Metadata Tracking

✅ Semantic Retrieval

✅ Context Construction

✅ Groq LLM Integration

✅ Source Attribution

✅ Multi-Document Legal Question Answering

---

# Technologies Used

* Python
* ChromaDB
* Sentence Transformers
* all-MiniLM-L6-v2
* Groq
* Llama 3.3 70B
* dotenv

---

# Next Steps (Day 12)

RAG Evaluation Framework

Topics:

* Recall@K
* Precision@K
* Ground Truth Dataset
* Hallucination Detection
* Retrieval Failure Analysis
* Evaluation Metrics

Goal:

Measure how good the RAG system actually is rather than simply verifying that it works.
