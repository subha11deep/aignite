import streamlit as st
from login_as_user import login_as_user

def register_page():
    # Center the title at the top
    st.markdown("<h1 style='text-align: center;'>Register</h1>", unsafe_allow_html=True)

    # Input fields for registration
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", placeholder="Enter your password", type="password")  # Password field
    age = st.number_input("Age", min_value=1, max_value=120, step=1, format="%d")
    policyname = st.text_input("Policy Name", placeholder="Enter your policy name")

    # File upload for prescription
    uploaded_file = st.file_uploader("Upload Prescription (PDF only)", type=["pdf"])

    # Submit button
    if st.button("Submit"):
        if username and password and age and policyname and uploaded_file:
            st.success("Registration successful!")
            st.write(f"Username: {username}")
            st.write(f"Age: {age}")
            st.write(f"Policy Name: {policyname}")
            st.write(f"Uploaded File: {uploaded_file.name}")
            # Forward to login page
            st.session_state.page = "login_as_user"
        else:
            st.error("Please fill in all fields and upload a prescription.")

    if st.button("Back to Main"):
        st.session_state.page = "main"  # Navigate back to Main Page