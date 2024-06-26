import unittest
from elasticsearch import Elasticsearch
from pdf_reader import load_pdf_file
from vector_store import set_vector_store
from chat_retrieval import retrieve_chat_response
from utils import set_keys
from dotenv import load_dotenv
from unittest.mock import patch
import os


class RAGTestCases(unittest.TestCase):
    # TODO: add unit tests for all functions

    # integration test for 4 suggested user questions
    @patch('builtins.input', side_effect=["Which two companies created the R.31 reconnaissance aircraft?", "What guns were mounted on the Renard R.31?", "Who was the first softball player to represent any country at four World Series of Softball?", "Who were the pitchers on the Australian softball team's roster at the 2020 Summer Olympics?"])
    def test_user_questions(self, value):
        # set_keys()
        load_dotenv('.env')
        openai_api_key = os.getenv('OPENAI_API_KEY')
        elastic_cloud_id = os.getenv("ELASTIC_CLOUD_ID")
        elastic_cloud_password = os.getenv("ELASTIC_CLOUD_PASSWORD")
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

        client = Elasticsearch(
            cloud_id=elastic_cloud_id,
            basic_auth=("elastic", elastic_cloud_password)
        )

        full_pages = []
        for file in os.listdir("docs"):
            if file.endswith(".pdf"):
                full_pages += load_pdf_file(os.path.join("docs", file))

        es_vector_store = set_vector_store(client, "rag_test_data_pipeline", full_pages)
        for _ in range(4):
            question = input()
            print("Question: {}\n".format(question))
            reply = retrieve_chat_response(es_vector_store, openai_api_key, question)
            print("Response: {}\n".format(reply))


if __name__ == '__main__':
    unittest.main()