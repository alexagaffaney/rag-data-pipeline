from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.runnables import RunnableLambda


def retrieve_chat_response(es_vector_store, openai_api_key, input_question) -> str:
    retriever = es_vector_store.as_retriever(search_kwargs={"k": 3})

    # sets template for chat model to interpret questions
    template = """Answer the question with the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            # | RunnableLambda(inspect)  # uncomment if you want to print the context passed in the chain
            | prompt
            | ChatOpenAI(openai_api_key=openai_api_key)
            | StrOutputParser()
    )
    # calling openAI with input question based on context searched from documents
    reply = chain.invoke(input_question)
    return reply


def inspect(state):
    # Print the state used in context for retriever
    print(state)
    return state
