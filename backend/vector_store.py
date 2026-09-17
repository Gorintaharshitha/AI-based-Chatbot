from langchain_community.vectorstores import FAISS
from backend.embeddings import embeddings


def load_vector_store():

    vector_store = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store