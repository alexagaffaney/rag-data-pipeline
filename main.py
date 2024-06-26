from elasticsearch import Elasticsearch
from pdf_reader import load_pdf_file
from vector_store import set_vector_store
from chat_retrieval import retrieve_chat_response
from utils import set_keys
from utils import set_env
from dotenv import load_dotenv
import os

index_name = "rag_data_pipeline"


def main():
    set_env()
    # set_keys()  # uncomment to write pass keys to .env file

    # Load variables from .env file
    load_dotenv('.env')

    # Get ENV variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    elastic_cloud_id = os.getenv("ELASTIC_CLOUD_ID")
    elastic_cloud_password = os.getenv("ELASTIC_CLOUD_PASSWORD")
    line = os.getenv("LINE_PRINT")

    if (not openai_api_key or not elastic_cloud_id or not elastic_cloud_password):
        raise ValueError("Please provide proper credentials: OpenAI API Key, Elastic Cloud ID, and Elastic Cloud Password")

    print("\n{}\nRunning RAG Test Data Pipeline\n{}\n".format(line, line))

    client = Elasticsearch(
        cloud_id=elastic_cloud_id,
        basic_auth=("elastic", elastic_cloud_password)
    )

    # test connection to Elasticsearch
    print("Setting connection to Elasticsearch with client: {}".format(client.info()))

    # load PDF pages into Elasticsearch Vector Store
    full_pages = []
    for file in os.listdir("docs"):
        if file.endswith(".pdf"):
            full_pages += load_pdf_file(os.path.join("docs", file))
    es_vector_store = set_vector_store(client, index_name, full_pages)

    print("\n{}\nType your questions below\nHit Enter or Ctrl+C to quit\n{}\n".format(line, line))

    while True:
        try:
            question = input("Question: ")
            if not question:
                raise ValueError
            reply = retrieve_chat_response(es_vector_store, openai_api_key, question)
            print("Answer: {}\n".format(reply))
        except:
            print("\n{}\nEnding RAG Test Data Pipeline\n{}\n".format(line, line))
            break


if __name__ == '__main__':
    main()
