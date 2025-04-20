import streamlit as st

def general_query_page():
    st.markdown("<h1 style='text-align: center;'>General Query</h1>", unsafe_allow_html=True)
    st.write("This page will help you with general queries.")
    if st.button("Back to Previous page"):
        st.session_state.page = "post_login"