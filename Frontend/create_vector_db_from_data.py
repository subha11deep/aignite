from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import pytesseract
import os
import time
import warnings

warnings.filterwarnings('ignore')
load_dotenv(find_dotenv())

# Setup Tesseract (if needed for OCR via unstructured)
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH", "C:/Program Files/Tesseract-OCR/tesseract.exe")

# Folder path for PDFs
folder_path = os.getenv("folder_path")
doc_list = []

# Load PDF documents
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        file_path = os.path.join(folder_path, filename)
        print(f"Loading: {file_path}")
        loader = UnstructuredPDFLoader(file_path)
        doc = loader.load()
        doc_list.append(doc)

# Initialize GROQ Chat model
llm = ChatGroq(
    api_key='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',
    model="llama3-8b-8192"  # or llama3-70b-8192, gemma-7b-it, etc.
)

# Use HuggingFace for embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"  # Or other open-source models
)

# Text splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
docs = []
for doc in doc_list:
    docs.extend(text_splitter.split_documents(doc))

# Store in FAISS in batches
BATCH_SIZE = 20

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

db = process_in_batches(docs, BATCH_SIZE, embeddings)

# Save FAISS DB locally
save_directory = os.getenv("save_directory")
db.save_local(save_directory)

print("✅ Embedding and storage complete using GROQ + HuggingFace")
