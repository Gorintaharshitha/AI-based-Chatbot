import os
from dotenv import load_dotenv

from backend.scraper import scrape_website
from backend.text_processor import create_chunks
from backend.embeddings import embeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


load_dotenv()

URL = "https://brightevents.in/"


def create_vector_db():

    print("Scraping website...")

    text = scrape_website(URL)

    print("Creating chunks...")

    chunks = create_chunks(text)

    print("Total chunks:", len(chunks))

    documents = [
        Document(page_content=chunk)
        for chunk in chunks
    ]

    print("Creating FAISS vector database...")

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    vector_store.save_local("vector_db")

    print("FAISS vector database created successfully.")


if __name__ == "__main__":
    create_vector_db()