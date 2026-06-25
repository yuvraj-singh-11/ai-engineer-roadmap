# Day 13 - Hybrid Search for Legal RAG

## Objective

Implement a Hybrid Retrieval System that combines:

- BM25 Keyword Search
- Vector Similarity Search using ChromaDB
- Reciprocal Rank Fusion (RRF)

This approach improves retrieval quality by combining exact keyword matching with semantic understanding.

---

## Concepts Covered

### Sparse Retrieval

Uses exact keyword matching.

Examples:

- BM25
- TF-IDF

Advantages:

- Fast
- Finds exact legal terms

Limitations:

- Cannot understand semantic meaning

---

### Dense Retrieval

Uses embeddings and vector similarity.

Advantages:

- Understands meaning
- Retrieves semantically related content

Limitations:

- Can miss exact legal terminology

---

### Hybrid Retrieval

Combines:

BM25 + Vector Search

Benefits:

- Better recall
- Better precision
- More reliable retrieval

---

## Architecture

User Query
│
├── BM25 Search
│
├── Vector Search (ChromaDB)
│
└── Reciprocal Rank Fusion (RRF)
│
▼
Final Ranked Results

---

## Project Structure

```text
day13-hybrid-search/
│
├── data/
├── bm25_search.py
├── vector_search.py
├── hybrid_search.py
├── main.py
└── README.md
```

## Technologies Used

- Python
- ChromaDB
- Sentence Transformers
- rank-bm25
- all-MiniLM-L6-v2

## Sample Queries

- termination clause
- confidential information
- indemnification
- governing law
- liability limitation

## Observations

### BM25

Strong for exact legal keywords.

### Vector Search

Strong for semantic similarity.

### Hybrid Search

Produced more balanced retrieval results.

### Limitation

RRF can occasionally promote noisy results because it considers ranking positions rather than similarity scores.

---

## Key Learnings

- Sparse vs Dense Retrieval
- BM25 Fundamentals
- Vector Similarity Search
- Hybrid Search Architecture
- Reciprocal Rank Fusion
- Production RAG Retrieval Strategies

---

## Future Improvements

- Cross-Encoder Re-ranking
- Metadata Filtering
- Query Expansion
- Hybrid Search Evaluation
- Multi-Vector Retrieval

---

## Outcome

Successfully implemented a Hybrid Search Pipeline for Legal AI applications using BM25, ChromaDB, and Reciprocal Rank Fusion.