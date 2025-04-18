# using 1 csv file and azure  
# from langchain.agents import AgentType 
# from langchain_experimental.agents.agent_toolkits import create_csv_agent 
# from langchain_openai import AzureChatOpenAI 
# from langchain_openai import AzureOpenAIEmbeddings 
# from langchain_community.vectorstores.faiss import FAISS 
# from langchain.chains import RetrievalQA 
# from dotenv import load_dotenv, find_dotenv 
# # import os  
# load_dotenv(find_dotenv()) 
# #Load your Faiss index 
# embeddings = AzureOpenAIEmbeddings(deployment='embeddings', azure_endpoint=os.getenv("azure_endpoint"), openai_api_key=os.getenv("AZURE_OPENAI_API_KEY 
# vectorstore = FAISS.load_local( os.getenv("save_directory"), embeddings, allow_dangerous_deserialization=True I  
# )

# # Define your LLM # llm_openai = AzureChatOpenAI( azure_endpoint=os.getenv("azure_endpoint"), 
    # azure_deployment=os.getenv("azure_deployment") 
    # api_version=os.getenv("api_version"), 
    # openai_api_key=os.getenv("AZURE_OPENAT_API_KEY"),
    # temperature=os.getenv("temperature") 
    # verbose=True  
    #)
# Create a RetrievalQA chain
# qa_chain = RetrievalQA.from_chain_type(llm=llm_openai, chain_type="stuff", retriever=vectorstore.as_retriever()) 

# Create an agent using the RetrievalQA chain 
# llm = create_csv_agent( qa_chain, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS, allow_dangerous_code=True ) Opt-in to allow execution of arbitrary code  

# print(.run("What is the latest research on colon cancer?"))  
 

# using faiss vector db and azure 
from langchain.agents import Tool, AgentType, initialize_agent 
from langchain_openai import AzureChatopenAI 
from langchain_openai import AzureOpenAIEmbeddings 
from langchain_community.vectorstores.faiss import FAISS 
from langchain.chains import RetrievalQA 
from dotenv import load_dotenv, find_dotenv 
import os

load_dotenv(find_dotenv())

# Load your Faiss index 
embeddings = AzureOpenAIEmbeddings(deployment='embeddings', azure_endpoint=os.getenv("azure_endpoint"), openai_api_key=os.getenv("AZURE_OPENAI_API_KEY")) 
vectorstore = FAISS.load_local( os.getenv("save_directory"), embeddings, allow_dangerous_deserialization=True )

# Define your LLM 
llm_openai = AzureChatOpenAI(azure_endpoint=os.getenv("azure_endpoint"), 
                             azure_deployment=os.getenv("azure_deployment"),
                            api_version=os.getenv("api_version"), 
                            openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                            temperature=os.getenv("temperature"),
                            verbose=True
                            )

# Create a RetrievalQA chain 
qa_chain = RetrievalQA.from_chain_type(llm=llm_openai, chain_type="stuff", retriever=vectorstore.as_retriever())

# Define a tool for using the RetrievalQA chain 
tool = Tool(
    name="Faiss Search",
    func=qa_chain.run, 
    description="""You are a helpful doctor's chatbot assistant,assisting.
    Based on the user query,first analyse the document and provide a very detailed response accordingly.
    If relevant answer is not present in the document,provide appropriate and detailed medically correct responses from medical documents. 
    If relevant answer is not present in document,do not mention the same in the answer. 
    Also ,always mention the source web link in the end, from where you found the response""")

# Initialize the agent 
llm = initialize_agent( 
    [tool], 
    llm_openai, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)
#using faiss vector db and gemini  
# from langchain.agents import Tool, AgentType, initialize_agent # 
# from langchain_google_genai import ChatGoogleGenerativeAI 
## from langchain.llms import Gemini 
# from langchain.experimental.embeddings import GeminiEmbeddings 
# from langchain_community.vectorstores.faiss import FAISS 
# from langchain.chains import RetrievalQA 
# from dotenv import load_dotenv, find_dotenv  
# import os  

# load_dotenv(find_dotenv())  
# Load your Faiss index 
# embeddings = GeminiEmbeddings(model_name="gemini-1.5-flash", api_key=os.getenv( "GEMINI_API_KEY")) 
# vectorstore = FAISS.load_local( os.getenv("save_directory"), embeddings, allow_dangerous_deserialization=True )  
# # Define your LLM 
# llm_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash" , google_api_key=os.getenv("GEMINI_API_KEY"), temperature=float(os.getenv("temperature"))) 

# # Create a RetrievalQA chain 
# qa_chain = RetrievalQA.from_chain_type(llm=llm_gemini, chain_type="stuff" , retriever=vectorstore.as_retriever()) 

# # Define a tool for using the RetrievalQA chain
#tool = Tool( 
# name="Faiss Search",
# func=qa_chain.run, 
# description="""You are a helpful doctor's chatbot assistant, assisting.
#  Based on the user query, first analyze the document and provide a very detailed response accordingly 
# If relevant answer is not present in the document, provide appropriate and detailed medically correct responses 
# from medical documents If relevant answer is not present in document, do not mention the same in the answer. 
# Also, always mention the source web link in the end, from where you found the response."""  )

# # Initialize the agent 
# llm = initialize_agent( 
    #[tool], 
    # llm_gemini, 
    # agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    # verbose=True
    # )  

