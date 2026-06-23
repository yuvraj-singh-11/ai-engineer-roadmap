# Day 10 - OpenAI/Groq Powered Legal RAG

## Objective

Build a Retrieval-Augmented Generation (RAG) system capable of answering questions from legal documents using:

* ChromaDB
* Sentence Transformers
* Groq LLM
* Semantic Search

---

## Architecture

User Question
↓
Sentence Transformer
↓
Query Embedding
↓
ChromaDB Similarity Search
↓
Top-K Chunks
↓
Prompt Builder
↓
Groq LLM
↓
Final Answer

---

## Project Structure

day10-openai-rag/

├── data/
│   └── nda.txt
│
├── ingest.py
├── retrieve.py
├── groq_client.py
├── prompts.py
├── rag.py
│
├── chroma_db/
├── requirements.txt
├── README.md
└── .env

---

## Installation

```bash
pip install -r requirements.txt
```

Create .env file:

```env
GROQ_API_KEY=your_api_key
```

---

## Ingestion

Run:

```bash
python ingest.py
```

Expected Output:

```text
Document Loaded
Chunks Created
Embeddings Generated
Stored in ChromaDB
```

---

## Run RAG

```bash
python rag.py
```

Example:

Question:

What is the confidentiality period?

Answer:

The confidentiality obligations survive termination for five years.

---

## Sample Questions

What is the confidentiality period?

Who owns intellectual property?

What is the governing law?

What are the termination conditions?

What must happen to confidential information after termination?

---

## Key Concepts Learned

* Embeddings
* Vector Databases
* ChromaDB
* Similarity Search
* Top-K Retrieval
* Retrieval-Augmented Generation
* Prompt Grounding
* Hallucination Prevention
* Legal AI Foundations

---

## Limitations

* No reranking
* No citations
* Single document support
* No evaluation framework
* No hybrid search

---

## Future Improvements

* Multi-document retrieval
* Metadata filtering
* Citations
* Reranking
* LangGraph agents
* Legal clause extraction
* Evaluation metrics

---

