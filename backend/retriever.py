from backend.vector_store import load_vector_store


def create_retriever():

    vector_store = load_vector_store()

    k = len(vector_store.index_to_docstore_id)

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": k
        }
    )

    return retriever