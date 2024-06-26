# RAG Test Data Pipeline
This is a test project done for BambooHR to set up a RAG pipeline to respond to user questions.

### Pipeline Details
This project performs the following steps:
1. Reads in all .pdf input files in the /docs directory
2. Splits the input files into individual pages
3. Creates an Elasticsearch client using Cloud ID and Cloud Password (see Setting Up Credentials section below)
4. Sets up index ("rag_data_pipeline") with basic mapping
5. Creates a Vector Store using the HuggingFaceEmbeddings embeddings model
6. Sets a template to send to OpenAI using:
   1. User inputted question
   2. Context from document store search based on user question (uncomment RunnableLambda(inspect) line in chat_retrieval.py to print context)
7. Prints response from OpenAI

### Setting up Credentials
> Follow **[this doc](https://platform.openai.com/docs/quickstart#:~:text=First%2C%20create%20an%20OpenAI%20account,not%20share%20it%20with%20anyone.)** for getting an Open AI Key \
> Log in to **[Elastic Cloud](https://cloud.elastic.co/login)** or **[sign up for a free trial](https://cloud.elastic.co/registration)**  to retrieve your Elastic Cloud ID and Cloud Password

For the first time running this pipeline: uncomment the set_keys() function in main() main.py to write the following credentials into an .env file:
- OPENAI_API_KEY 
- ELASTIC_CLOUD_ID 
- ELASTIC_CLOUD_PASSWORD

### Packages Used
Use below imports to install packages used in this pipeline\
```bash
pip3 install elasticsearch
pip3 install PyPDF2
pip3 install pandas
pip3 install langchain
pip3 install urllib
pip3 install langchain-community
pip3 install pypdf
pip3 install sentence-transformers
pip3 install openai
pip3 install langchain-openai
pip3 install langchain_community
pip3 install langchain-huggingface
pip3 install python-dotenv
```
_*assumes python 3 usage - use pip instead if you are not using python3_

### Future Work
- Containerize pipeline to create self contained environment to run the project
- Add more test cases for greater functionality checks
- Add more input validation checks
- Look into other ways to index input documents or other embedding models

### Sources
Check out the below guides that were used as reference for this project:
- [OpenAI Cookbook RAG](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/elasticsearch/elasticsearch-retrieval-augmented-generation.ipynb)
- [RAG Pipeline with ChatGPT, Langchain, and ElasticSearch](https://blog.gigasearch.co/rag-elasticsearch/)
- [Hugging Embeddings Sentence Transformer Model](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [ElasticSearch 8.0 Migration guide](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/migration.html)
- [Indexing a PDF into ElasticSearch](https://kb.objectrocket.com/elasticsearch/how-to-index-a-pdf-file-as-an-elasticsearch-index-267)