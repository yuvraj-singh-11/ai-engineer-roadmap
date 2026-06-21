# Day 08 - Advanced Document Chunking

## Overview

This project demonstrates one of the most important concepts in Retrieval-Augmented Generation (RAG) systems: **Document Chunking**.

Large documents such as contracts, policies, due diligence reports, and legal agreements cannot be embedded effectively as a single unit. Instead, they are split into smaller chunks that can be indexed, searched, and retrieved efficiently.

This project implements:

* Document Loading
* Text Chunking
* Chunk Overlap
* Chunk Metadata Generation
* Foundation for Production RAG Pipelines

---

## Learning Objectives

By completing this project, I learned:

* Why chunking is necessary in RAG systems
* Why entire documents should not be embedded as a single vector
* How chunk overlap preserves context
* How chunk size affects retrieval quality
* How production ingestion pipelines prepare documents for vector databases

---

## Project Structure

```text
day08-document-chunking/
│
├── contracts/
│   └── vendor_agreement.txt
│
├── loader.py
├── chunker.py
├── main.py
│
├── README.md
└── requirements.txt
```

---

## Architecture

```text
Contract Document
        │
        ▼
Document Loader
        │
        ▼
Chunking Engine
        │
        ▼
Chunk Overlap Logic
        │
        ▼
Structured Chunks
        │
        ▼
Ready For Embeddings
        │
        ▼
Vector Database
```

---

## Why Chunking Is Required

### Problem

Embedding an entire legal contract as a single vector causes:

* Loss of semantic precision
* Poor retrieval quality
* High embedding costs
* Large context windows

Example:

```text
100 Page Contract
      ↓
Single Embedding
```

The resulting vector becomes an average representation of the entire document.

Important sections such as:

* Termination
* Liability
* Confidentiality
* Payment Terms

become difficult to retrieve accurately.

---

### Solution

Split the document into smaller chunks.

```text
100 Page Contract
      ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

Each chunk is embedded independently.

This improves retrieval precision significantly.

---

## Chunk Overlap

Chunk overlap preserves context between neighboring chunks.

Example:

```text
Chunk 1
------------------
Termination clause starts here

Chunk 2
------------------
starts here and continues...
```

Without overlap:

* Sentences can be broken
* Important context may be lost

With overlap:

```text
Chunk 1
0 ---------- 500

Chunk 2
400 -------- 900

Overlap = 100
```

Both chunks share part of the content.

This improves retrieval quality.

---

## Implementation Details

### Document Loader

Responsible for reading text files.

```python
def load_document(file_path):
    ...
```

Output:

```python
str
```

---

### Chunking Engine

Responsible for splitting text into chunks.

```python
def chunk_text(
    text,
    chunk_size=500,
    overlap=100
):
    ...
```

Parameters:

| Parameter  | Description                      |
| ---------- | -------------------------------- |
| chunk_size | Maximum chunk length             |
| overlap    | Shared characters between chunks |

---

## Example Output

Document Length:

```text
876 characters
```

Chunk Configuration:

```text
Chunk Size = 500
Overlap = 100
```

Output:

```text
Chunk 1
Chunk 2
Chunk 3
```

---

## Interview Questions

### Why not embed an entire contract?

Embedding an entire contract creates a single vector representing many unrelated topics. This reduces retrieval accuracy because important sections become diluted within the overall document representation.

---

### What is chunk overlap?

Chunk overlap is a technique where neighboring chunks share content. This prevents loss of context at chunk boundaries and improves retrieval quality.

---

### How does chunk size affect retrieval?

Small chunks:

* Better precision
* Less context

Large chunks:

* More context
* Lower precision

Choosing an appropriate chunk size is a tradeoff.

---

### What happens if overlap is too large?

Benefits:

* Better context preservation

Drawbacks:

* More storage
* More embeddings
* Higher processing cost

---

## Real-World Legal AI Applications

This technique is used in:

* Contract Review Systems
* Due Diligence Platforms
* Legal Research Assistants
* Compliance Monitoring Systems
* Enterprise Knowledge Bases
* RAG-Based Legal Chatbots

---

## Key Takeaways

* Chunking is the foundation of production RAG systems.
* Large documents should not be embedded as a single vector.
* Chunk overlap improves context retention.
* Retrieval quality depends heavily on chunking strategy.
* Proper chunking significantly improves answer accuracy.

---

## Next Step

Day 09 – Retrieval Pipeline

```text
Contract
   ↓
Chunking
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Top-K Retrieval
```

This will transform the chunked documents into a searchable knowledge base.
21/06/2026
