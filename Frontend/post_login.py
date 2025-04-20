import streamlit as st

def post_login_page():
    # Center the title at the top
    st.markdown("<h1 style='text-align: center;'>Welcome!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Choose any option below:</h3>", unsafe_allow_html=True)

    # Display the 5 options as buttons
    if st.button("Health Policy Assistant"):
        print("Health Policy Assistant")
        st.session_state.page = "health_policy"
        print("Health Policy Assistant2")

    if st.button("Symptoms Query"):
        print("Symptoms Query")
        st.session_state.page = "disease_query"
        print("Symptoms Query2")

    # if st.button("General Query"):
    #     st.session_state.page = "general_query"

    if st.button("Select/Upload Prescription"):
        st.session_state.page = "prescription"

    if st.button("Select Your Language"):
        st.session_state.page = "language_selection"
    if st.button("Back to Main"):
        st.session_state.page = "main"  # Navigate back to Main Page