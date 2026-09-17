from backend.retriever import create_retriever
from backend.chatbot import generate_answer


def main():

    print("BrightEvents AI Chatbot")
    print("Type 'exit' to stop.")

    retriever = create_retriever()

    while True:

        query = input("\nYOU: ")

        if query.lower().strip() == "exit":
            print("Chatbot ended.")
            break

        retrieved_docs = retriever.invoke(query)

        answer = generate_answer(
            query,
            retrieved_docs
        )

        print("\nBOT:", answer)


if __name__ == "__main__":
    main()