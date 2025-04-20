from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv
import os
import traceback
import warnings

warnings.filterwarnings("ignore")
load_dotenv(find_dotenv())

# Load vector store with HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

# Load FAISS vectorstore
save_directory = os.getenv("save_directory")
if not save_directory:
    raise ValueError("The 'save_directory' environment variable is not set.")
if not os.path.exists(os.path.join(save_directory, "index.faiss")):
    raise FileNotFoundError(f"The FAISS index file 'index.faiss' is missing in the directory: {save_directory}")

# Load FAISS vectorstore
new_vector_store = FAISS.load_local(
    save_directory,
    embeddings,
    allow_dangerous_deserialization=True
)

# Question to ask
question = """I am going for a cosmetic surgery.Will this be covered as a part of my health insurance policy? """




# Function to query LLM using GROQ
def genai_query_answer(question):
    print(f"Received question: {question}")  # Debugging statement
    if not question:
        question = """I am going for a cosmetic surgery.Will this be covered as a part of my health insurance policy? """

    # Retrieve relevant docs
    docs_db = new_vector_store.similarity_search_with_score(question)
    # Initialize GROQ LLM
    llm = ChatGroq(
        api_key="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",
        model="llama3-8b-8192"  
    )

    input = question
    context = "\n".join([str(doc[0].page_content) for doc in docs_db])

    prompt_template = """I am a medical health policy assistant.I am guiding policy owners,their respective query on this policy.
                        I am guiding them whether this particular treatment/procedure is covered under the policy or not.
                        I am also guiding them on the reason for the coverage or non-coverage of the treatment/procedure.
                        I am answering both simple and complex queries with ease.
User query: {input} 
Document: {context}
"""

    prompt = PromptTemplate(input_variables=['input', 'context'], template=prompt_template)
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    try:
        print(f"Input: {input}")
        print(f"Context: {context[:1000]}...")  # Print only the first 1000 chars
        response = llm_chain.invoke({'input': input, 'context': context})
        return response['text']
    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        return None


# # Run the response function
# test_response = genai_query_answer(question, docs_db)
# print(test_response)
