import streamlit as st

def login_as_user():
    st.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", placeholder="Enter your password", type="password")
    if st.button("Submit"):
        if username and password:
            st.success("Login successful!")
            st.session_state.page = "post_login"
        else:
            st.error("Please enter both username and password.")
    if st.button("Back to Main"):
        st.session_state.page = "main"  # Navigate back to Main Page