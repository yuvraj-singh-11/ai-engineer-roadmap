import json
from rank_bm25 import BM25Okapi


class BM25Search:
    def __init__(self, chunks_file="chunks.json"):
        with open(chunks_file, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)
            
        # Tokenize corpus
        tokenized_corpus = [self._tokenize(doc["text"]) for doc in self.chunks]
        self.bm25 = BM25Okapi(tokenized_corpus)

    def _tokenize(self, text: str):
        return text.lower().split()

    def search(self, query: str, k: int = 5):
        tokenized_query = self._tokenize(query)
        doc_scores = self.bm25.get_scores(tokenized_query)
        
        # Sort and get top k
        top_indices = sorted(range(len(doc_scores)), key=lambda i: doc_scores[i], reverse=True)[:k]
        
        results = []
        for idx in top_indices:
            chunk = self.chunks[idx]
            results.append({
                "text": chunk["text"],
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "score": round(doc_scores[idx], 6)
            })
            
        return results


if __name__ == "__main__":
    searcher = BM25Search()
    results = searcher.search("termination clause", k=3)
    for r in results:
        print(f"[{r['source']}:{r['chunk_id']}] Score: {r['score']}")
