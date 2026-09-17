from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.retriever import create_retriever
from backend.chatbot import generate_answer


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


retriever = create_retriever()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "BrightEvents AI chatbot Backend is running!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    query = request.message

    retrieved_docs = retriever.invoke(query)

    answer = generate_answer(
        query,
        retrieved_docs
    )

    return {
        "answer": answer
    }