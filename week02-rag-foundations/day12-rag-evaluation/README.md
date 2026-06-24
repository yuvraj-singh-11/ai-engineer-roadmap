# Day 12 — RAG Evaluation (Legal Documents)

This project evaluates retrieval quality for a legal-domain RAG pipeline using ChromaDB + MiniLM embeddings.

---

## 📁 Project Structure

```text
day12-rag-evaluation/
├── data/
│   ├── nda.txt
│   ├── employment.txt
│   └── msa.txt
├── chroma_db/
├── ingest.py
├── query.py
├── evaluator.py
├── test_questions.py
├── main.py
└── README.md
```

---

## 🎯 Goal

Measure and improve retrieval quality using:

- **Hit@K**
- **Source Recall@K**
- **Source Precision@K**
- **Keyword Coverage**

This helps detect:
- missed sources in cross-document questions,
- noisy retrieval in single-document factual questions,
- impact of `k`, chunking, and reranking strategy.

---

## ⚙️ Setup

## 1) Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2) Install dependencies
```bash
pip install chromadb sentence-transformers langchain-text-splitters
```

---

## 📥 Step 1: Ingest Documents

Run ingestion to load `.txt` files, chunk, embed, and store in ChromaDB:

```bash
python3 ingest.py
```

Expected output includes:
- number of documents loaded,
- number of chunks created,
- confirmation that chunks were stored.

---

## 🔎 Step 2: Run Evaluation

```bash
python3 main.py
```

This evaluates all questions in `test_questions.py` and prints:
- per-question retrieved sources/chunks,
- per-question metrics,
- overall summary metrics.

---

## 🧠 Retrieval Modes

`query.py` supports:

1. **Standard retrieval** (`retrieve`)
   - Best for single-document fact questions.

2. **Diverse retrieval** (`retrieve_diverse`)
   - Two-stage strategy:
     - retrieve top `initial_k` by similarity,
     - rerank to improve source diversity.
   - Best for cross-document questions (e.g., “Which agreements…”).

Recommended routing in `main.py`:
- cross-doc questions → `retrieve_diverse(...)`
- fact questions → `retrieve(...)`

---

## 📊 Metrics Explained

- **Hit@K**  
  `1` if any expected source appears in top-K, else `0`.

- **Source Recall@K**  
  Fraction of expected sources covered in top-K.  
  Example: expected 3 sources, found 2 → recall = `2/3 = 0.6667`.

- **Source Precision@K**  
  Fraction of unique retrieved sources that are expected.  
  High value = less source noise.

- **Keyword Coverage**  
  Fraction of expected keywords found in retrieved top-K context.

---

## 🧪 Experiments to Run

Test these settings and compare summary metrics:

1. `k=3` (baseline)
2. `k=5`
3. `k=10`
4. standard retrieval vs diverse retrieval
5. optional chunk experiments:
   - chunk_size=200, overlap=50
   - chunk_size=300, overlap=60
   - chunk_size=400, overlap=80

---

## ✅ Common Debug Checks

## Check if `msa.txt` chunks exist in Chroma
```bash
python3 - << 'PY'
import chromadb
client = chromadb.PersistentClient(path="./chroma_db")
col = client.get_or_create_collection(name="legal_documents")
res = col.get(where={"source": "msa.txt"}, include=["metadatas"], limit=5)
print("Count:", len(res["ids"]))
print("Sample IDs:", res["ids"][:5])
PY
```

## Inspect top-20 retrieval for a query
```bash
python3 - << 'PY'
from query import LegalRetriever
r = LegalRetriever()
q = "Which agreements contain termination clauses?"
res = r.retrieve(q, k=20)
for i, x in enumerate(res, 1):
    print(i, x["source"], x["chunk_id"], x["score"])
PY
```

## Test diverse retrieval quickly
```bash
python3 - << 'PY'
from query import LegalRetriever
r = LegalRetriever()
q = "Which agreements contain termination clauses?"
res = r.retrieve_diverse(q, k=5, initial_k=20)
for i, x in enumerate(res, 1):
    print(i, x["source"], x["chunk_id"], x["score"])
PY
```

---

## ⚠️ Notes

- HF warning about unauthenticated requests is normal; optional to set `HF_TOKEN`.
- Keep file names in `test_questions.py` exactly matching files in `data/`.
- If metrics look too perfect, verify your metric logic for multi-source questions.

---

## 🚀 Next Improvements

- Query expansion for legal synonyms (`terminate`, `cease`, `discontinue`, `suspend`).
- Section-aware chunking (clause/header based).
- Add reranking model.
- Add generation evaluation (faithfulness/citation correctness).

---
```