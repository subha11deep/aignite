import streamlit as st

def login_as_admin():
    # Title for the admin login page
    st.markdown("<h1 style='text-align: center;'>Admin Login</h1>", unsafe_allow_html=True)

    # Input fields for admin login
    admin_username = st.text_input("Admin Username", placeholder="Enter your admin username")
    admin_password = st.text_input("Admin Password", placeholder="Enter your admin password", type="password")

    # Login button
    if st.button("Login"):
        if admin_username and admin_password:  # Replace with actual authentication logic
            st.success("Login successful!")
            st.session_state.page = "admin_dashboard"  # Navigate to admin dashboard (to be implemented)
        else:
            st.error("Invalid username or password. Please try again.")

    # Back button to navigate to the main page
    if st.button("Back to Main"):
        st.session_state.page = "main"