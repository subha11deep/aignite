import streamlit as st
from components.chat_utils import ChatAgent 
from components.prompts import chat_prompt_template 
from components.llm import llm 
from PIL import Image  
def main(): 
    st.set_page_config( page_title="The AI Oncologist", 
                       page_icon='*',
                    layout="wide"
    )  
    # Define two columns - this will make layout split horizontally 
    col1, col2 = st.columns([1, 3])  
    # Place the logo in the first column 
    with col1: 
        image = Image.open("assets/arogya_mitra.jfif")
        resized_image = image.resize((400, 500)) 
        st.image(resized_image)  
    # In the second column, place text explaining the purpose of the app and some example scientific questions that your user might ask. 
    with col2: 
        st.title("Aarogya Mitra AI") 
        st.markdown(""" We are happy to help you with your queries.""")
    # This is the chatbot component 
    chat_agent = ChatAgent(prompt=chat_prompt_template, llm=llm) 
    chat_agent.start_conversation() 
    # chat_agent.run() 
if __name__ =="__main__": 
    main()  