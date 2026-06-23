from retrieve import retrieve_context
# pyrefly: ignore [missing-import]
from groq_client import ask_llm
from prompts import LEGAL_RAG_PROMPT


def answer_question(question):

    chunks = retrieve_context(
        question,
        k=5
    )

    context = "\n\n".join(chunks)

    prompt = LEGAL_RAG_PROMPT.format(
        context=context,
        question=question
    )

    answer = ask_llm(prompt)

    return answer


def main():

    print("=" * 60)
    print("LEGAL RAG ASSISTANT")
    print("=" * 60)

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":
            break

        answer = answer_question(
            question
        )

        print("\nAnswer:")
        print(answer)


if __name__ == "__main__":
    main()