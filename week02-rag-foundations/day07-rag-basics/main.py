# day07-rag-basics/main.py
from retrieve import retrieve_context
from rag import build_rag_prompt
from llm import ask_llm  # Swapped from mock response to real Groq client

def run_pipeline(user_query: str):
    print("="*50)
    print(f"1. DELIVERABLE: User Query\n   -> \"{user_query}\"")
    print("="*50)
    
    # Step 1: Semantic Search Retrieval
    retrieved_chunks = retrieve_context(user_query, n_results=1)
    print(f"2. DELIVERABLE: Retrieved Chunks\n   -> {retrieved_chunks}")
    print("="*50)
    
    # Step 2: Context Injection & Prompt Building
    final_prompt = build_rag_prompt(user_query, retrieved_chunks)
    print("3. DELIVERABLE: Final Prompt")
    print(final_prompt)
    print("="*50)
    
    # Step 3: Production Generation using Groq & Llama 3.1
    print("Sending engineered prompt to Groq...")
    answer = ask_llm(final_prompt)
    print(f"4. REAL LLM ANSWER:\n   {answer}\n")
    print("="*50)

if __name__ == "__main__":
    # Test with our indexed coffee machine data
    run_pipeline("What is the passcode for the coffee machine?")