# day07-rag-basics/rag.py

def build_rag_prompt(query: str, context_chunks: list) -> str:
    context_text = "\n".join([f"- {chunk}" for chunk in context_chunks])
    
    prompt = f"""You are a helpful assistant. Answer the question based ONLY on the provided context below. If the answer cannot be found in the context, say "I don't know".

---
CONTEXT:
{context_text}
---

QUESTION: {query}

ANSWER:"""
    return prompt

def generate_mock_llm_response(prompt: str) -> str:
    # This is the placeholder function we are replacing next!
    return "[Mock LLM Response] I have successfully received the context injected prompt!"