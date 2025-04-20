

import streamlit as st
import requests  # For API calls (replace with your actual API logic)
from answer_questions_from_vector_db import genai_query_answer  # Import your function for querying the GenAI model
def disease_query_page():
    # Initialize session state for disease query chat history
    if "disease_query_messages" not in st.session_state:
        st.session_state.disease_query_messages = []  # Stores the chat history for disease queries

    # Center the title at the top
    st.markdown("<h1 style='text-align: center;'>Symptom Query Assistant</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>Welcome to the Symptom Query Assistant. You can ask questions about symptoms, "
        "diseases, and related medical conditions. Our assistant will provide you with helpful information.</p>",
        unsafe_allow_html=True,
    )

    # Display chat history
    st.write("### Chat History")
    for message in st.session_state.disease_query_messages:
        if message["role"] == "user":
            st.markdown(f"<div style='text-align: right; color: blue;'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; color: green;'><b>Assistant:</b> {message['content']}</div>", unsafe_allow_html=True)

    # Input area for user text
    user_input = st.text_input("Type your message:", placeholder="Ask about diseases...")

    # Send button
    if st.button("Send"):
        if user_input.strip():
            # Add user message to chat history
            st.session_state.disease_query_messages.append({"role": "user", "content": user_input})

            # Call the API with the user input (replace with your actual API endpoint and logic)
            try:
                backend_response = genai_query_answer(user_input)
                # backend_response = "Thank you for your query. We will provide you with the necessary information soon."
                if backend_response:
                    # Add assistant response to chat history
                    st.session_state.disease_query_messages.append({"role": "assistant", "content": backend_response})
                else:
                    st.error("No response received from the assistant.")
                # Add assistant response to chat history
                st.session_state.disease_query_messages.append({"role": "assistant", "content": backend_response})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            

            # Add assistant response to chat history
            st.session_state.disease_query_messages.append({"role": "assistant", "content": backend_response})

    # Back button to navigate to the post-login page
    if st.button("Back to previous page"):
        st.session_state.page = "post_login"