from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.chains.question_answering.chain import load_qa_chain
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.llms import AzureOpenAI
import os
import pandas as pd
import time
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI 
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import (FewShotChatMessagePromptTemplate, ChatPromptTemplate)
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv
import warnings
warnings.filterwarnings('ignore')
import os
from langchain_community.chat_models import AzureChatOpenAI



load_dotenv(find_dotenv())
os.environ["OCR_AGENT"] = os.getenv("OCR_AGENT")

# folder_path = r"C:\Users\Subhadeep Mondal\Documents\gi_cancer\knowledge_repository"  
folder_path = os.getenv('folder_path')
doc_list = []
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        loader = UnstructuredPDFLoader(file_path)
        doc = loader.load()
        doc_list.append(doc)

embeddings = AzureOpenAIEmbeddings(deployment="embeddings", azure_endpoint=os.getenv("azure_endpoint"), openai_api_key=os.getenv("AZURE_OPENAI_API_KEY")) 

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20, length_function=len, is_separator_regex=False) 

docs = [] 
for i in range(0, len(doc_list)): 
    docs.append(text_splitter.split_documents(doc_list[i])) 
flat_list = [] 
for sublist in docs: 
    for item in sublist: 
       flat_list.append(item) 

BATCH_SIZE = 20 
db = None 
def process_in_batches(docs, batch_size, embeddings): 
    db = None 
    for i in range(0, len(docs), batch_size): 
       batch = docs[i:i + batch_size] 
       if db is None: 
          db = FAISS.from_documents(batch, embeddings) 
       else: 
          db.add_documents(batch) 
       time.sleep(1) 
    return db 

db = process_in_batches(flat_list, BATCH_SIZE, embeddings) 
save_directory = os.getenv("save_directory") 
db.save_local(save_directory) 
print("done")
