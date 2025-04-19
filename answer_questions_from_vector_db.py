from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain.chains.question_answering.chain import load_qa_chain
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain.llms import AzureOpenAI
import os
import pandas as pd
import time
from langchain_openai import AzureOpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import (
    FewShotChatMessagePromptTemplate,
    ChatPromptTemplate)
from langchain.chat_models import AzureChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains import LLMChain
# from keras.layers import Embedding

from dotenv import load_dotenv,find_dotenv 
import warnings
warnings.filterwarnings('ignore')
import os
embeddings = AzureOpenAIEmbeddings(deployment="embeddings", azure_endpoint=os.getenv("azure_endpoint"), openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"))
load_dotenv(find_dotenv())

new_vector_store = FAISS.load_local(os.getenv("save_directory"), embeddings, allow_dangerous_deserialization=True
                                    )
question = """Which part of the population is most affected by Stage IV Colorectal Cancer with liver metastases,and why certain interventions do not work for them? """
docs_db = new_vector_store.similarity_search_with_score(question)
def genai_query_answer(question, docs_db): 
    llm = AzureChatOpenAI( azure_endpoint=os.getenv("azure_endpoint") ,
                          azure_deployment=os.getenv("azure_deployment") ,
                          api_version=os.getenv("api_version"),
                          openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
                          temperature=os.getenv("temperature") 
    )
    input = question 
    context = str(docs_db) 
    prompt_template = """You are a helpful doctor's chatbot assistant,assisting .Based on the user query,first analyse the document 
    and provide a very detailed response accordingly If relevant answer is not present in the 
    document,provide appropriate and detailed medically correct responses from medical documents 
    If relevant answer is not present in document,do not mention the same in the answer 
    Also , always mention the source web link in the end,from where you found the response. 
    user query: {input} 
    document: {context}"""
    prompt = PromptTemplate(input_variables=['input','context'],template=prompt_template) 
    llm_chain=LLMChain(llm=llm,prompt=prompt) 
    try:
        response=llm_chain.invoke({'input': input, 'context': context}) 
        return response['text'] 
    except Exception as e:
        print(f"Error: {e}") 
        import traceback
        print(traceback.format_exc())
        return None
 
test_response=genai_query_answer(question, docs_db) 
# print(test_response.replace('\n', '\n\t')) 
print(test_response)