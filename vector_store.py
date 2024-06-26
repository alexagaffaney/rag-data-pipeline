from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import ElasticsearchStore


def set_vector_store(es, index_name, pages) -> ElasticsearchStore:
    # set embedding model to use for vector store
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # create vector store
    es_vector_store = ElasticsearchStore.from_documents(
        pages,
        es_connection=es,
        index_name=index_name,
        embedding=embeddings
    )

    return es_vector_store
