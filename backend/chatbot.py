import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=api_key,
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
    """
You are a helpful chatbot for BrightEvents.

Answer the user's question using ONLY the provided context.

Rules:
- Answer directly and briefly.
- Answer only what the user asked.
- Do not add unrelated information.
- Do not list other events or services unless the user asks for them.
- If the answer is available in the context, provide it.
- If the answer is not available in the context, say:
  "I don't know based on available BrightEvents information."

CONTEXT:
{context}

USER QUESTION:
{question}

Answer:
"""
)


def generate_answer(question, retrieved_docs):

    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(final_prompt)

    if isinstance(response.content, list):
        answer = response.content[0]["text"]
    else:
        answer = response.content

    return answer