# Day 14 - Cross Encoder Re-ranking for Legal RAG

## Objective

Implement a Cross Encoder Re-ranking stage on top of the Hybrid Retrieval pipeline built in Day 13.

The goal is to improve retrieval quality by re-scoring candidate chunks using a transformer model that evaluates the query and document chunk together.

---

## Learning Outcomes

By the end of this project, you will understand:

* Bi-Encoder Retrieval
* Cross Encoder Re-ranking
* Two-Stage Retrieval Architecture
* Retrieval vs Ranking
* Production RAG Pipelines
* Precision vs Recall Trade-offs

---

## Architecture

```text
User Query
      │
      ▼

Hybrid Search
(BM25 + ChromaDB)

      │
      ▼

Top 10 Chunks

      │
      ▼

Cross Encoder
(ms-marco-MiniLM-L-6-v2)

      │
      ▼

Top 3 Chunks

      │
      ▼

Final Context
```

---

## Project Structure

```text
day14-reranking/

├── data/
│
├── chroma_db/
│
├── bm25_search.py
├── vector_search.py
├── hybrid_search.py
├── reranker.py
├── main.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* ChromaDB
* Sentence Transformers
* rank-bm25
* Cross Encoder
* all-MiniLM-L6-v2

---

## Retrieval Pipeline

### Stage 1: Hybrid Retrieval

Combines:

* BM25 Keyword Search
* Dense Vector Search

Fusion Method:

```text
Reciprocal Rank Fusion (RRF)
```

Output:

```text
Top 10 Candidate Chunks
```

---

### Stage 2: Cross Encoder Re-ranking

Input:

```text
(Query, Chunk)
```

Example:

```text
termination clause

[SEP]

Either party may terminate this agreement...
```

Output:

```text
Relevance Score
```

Example:

```text
8.21
```

Chunks are sorted by relevance score.

---

## Bi-Encoder vs Cross Encoder

### Bi-Encoder

```text
Query → Embedding

Chunk → Embedding

Cosine Similarity
```

Advantages:

* Fast
* Scalable

Limitations:

* Less accurate

---

### Cross Encoder

```text
Query + Chunk

↓

Transformer

↓

Relevance Score
```

Advantages:

* Highly accurate

Limitations:

* Computationally expensive

---

## Sample Queries

* termination clause
* confidential information
* indemnification
* governing law
* liability limitation

---

## Observations

### Before Re-ranking

Hybrid retrieval occasionally returned noisy chunks.

Example:

```text
employment.txt
```

appearing in legal indemnification queries.

---

### After Re-ranking

Cross Encoder promoted:

```text
MSA indemnification clauses
```

and removed irrelevant chunks.

Retrieval quality improved significantly.

---

## Why Re-ranking Matters

Hybrid retrieval is optimized for:

```text
Recall
```

Cross Encoder is optimized for:

```text
Precision
```

Combining both produces higher-quality retrieval.

---

## Key Concepts Learned

* Dense Retrieval
* Sparse Retrieval
* Hybrid Search
* Reciprocal Rank Fusion
* Cross Encoder
* Two-Stage Retrieval
* Retrieval Precision
* Production RAG Architecture

---

## Interview Questions

### Why not use Cross Encoder directly on all documents?

Because it is computationally expensive.

Example:

```text
100,000 documents

×

Cross Encoder
```

would be too slow.

---

### Why retrieve first and rerank later?

To reduce search space.

```text
100,000 Chunks

↓

Top 10 Retrieved

↓

Cross Encoder

↓

Top 3 Results
```

---

### What is the difference between a Bi-Encoder and a Cross Encoder?

Bi-Encoder:

```text
Independent embeddings
```

Cross Encoder:

```text
Joint evaluation of query and chunk
```

---

## Future Improvements

* Metadata Filtering
* Query Expansion
* Multi-Query Retrieval
* RAG Evaluation
* Context Compression
* LLM Answer Generation

---

## Outcome

Successfully implemented a production-style two-stage retrieval architecture using:

* Hybrid Search (BM25 + Vector Search)
* Reciprocal Rank Fusion
* Cross Encoder Re-ranking

This architecture is commonly used in enterprise Legal AI and RAG systems.
