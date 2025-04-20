import streamlit as st
from answer_questions_from_vector_db import genai_query_answer  # Relative import
#from ..AI.create_vector_db_from_data import new_vector_store  # Relative import

def health_policy_page():
    # Initialize session state for health policy chat history
    print("chk1")
    if "health_policy_messages" not in st.session_state:
        st.session_state.health_policy_messages = []  # Stores the chat history for health policy queries

    # Center the title at the top
    st.markdown("<h1 style='text-align: center;'>Health Policy Assistant</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>Welcome to the Health Policy Assistant. You can ask questions about health policies, "
        "insurance plans, and related topics. Our assistant will provide you with the best possible answers.</p>",
        unsafe_allow_html=True,
    )

    # Display chat history
    st.write("### Chat History")
    for message in st.session_state.health_policy_messages:
        if message["role"] == "user":
            st.markdown(f"<div style='text-align: right; color: blue;'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; color: green;'><b>Assistant:</b> {message['content']}</div>", unsafe_allow_html=True)

    # Input area for user text
    user_input = st.text_input("Type your message:", placeholder="Ask about health policies...")
    if not user_input:
        user_input = "hello, i need help with my health policy"  # Default message for testing
    # Send button
    # backend_response = genai_query_answer(user_input)
    # print(backend_response)
    if st.button("Send"):
        if user_input.strip():
            # Add user message to chat history
            st.session_state.health_policy_messages.append({"role": "user", "content": user_input})

            # Call the genai_query_answer function with the user input
            try:
                backend_response = genai_query_answer(user_input)
                # backend_response = "Thank you for your query. We will provide you with the necessary information soon."
                if backend_response:
                    # Add assistant response to chat history
                    st.session_state.health_policy_messages.append({"role": "assistant", "content": backend_response})
                else:
                    st.error("No response received from the assistant.")
                # Add assistant response to chat history
                st.session_state.health_policy_messages.append({"role": "assistant", "content": backend_response})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

        # Back button to navigate to the post-login page
    if st.button("Back"):
        st.session_state.page = "post_login"