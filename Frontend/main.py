import streamlit as st
from register import register_page
from post_login import post_login_page
from health_policy import health_policy_page
from disease_query import disease_query_page
from general_query import general_query_page
from prescription import prescription_page
from language_selection import language_selection_page
from login_as_user import login_as_user
from login_as_admin import login_as_admin
from admin_dashboard import admin_dashboard_page
from dashboard import dashboard_page

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "main"  # Default page is "main"

# Function to navigate to a different page
def navigate_to(page_name):
    st.session_state.page = page_name

# Main Page
if st.session_state.page == "main":
    
    # Center the title at the top
    st.markdown(
        "<h1 style='text-align: center; font-size: 50px;'>Aarogyamitra AI</h1>",
        unsafe_allow_html=True,
    )
    st.write("##")
    # Welcome message
    st.markdown("<h2 style='text-align: center;font-size: 30px'>Welcome to your GenAI Medical Assistant</h2>", unsafe_allow_html=True)

    # Add spacing to move buttons to the middle
    st.write("##")
    # st.write("##")
    # st.write("##")
    # st.write("##")

    # Create buttons for Login and New User Register with adjusted spacing
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust column widths to shift the Login button

    with col1:
        if st.button("Login as admin", key="login_admin", help="Click to login as admin"):
            navigate_to("login_as_admin")  # Update session state to navigate to Login Page
            st.write("Redirecting to Login Page...")  # Placeholder for redirection logic
        pass  # Empty column for spacing on the left

    with col2:
        if st.button("Login as user", key="login", help="Click to login as user"):
            navigate_to("login_as_user")  # Update session state to navigate to Login Page
            st.write("Redirecting to Login Page...")  # Placeholder for redirection logic

    with col3:
        if st.button("New User Register", key="register", help="Click to register"):
            navigate_to("register")  # Update session state to navigate to Register Page
            st.write("Redirecting to Registration Page...")  # Placeholder for redirection logic
    
    # Add custom CSS to style buttons with blue color and larger size
    st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #007BFF;
        color: white;
        margin: 0 auto;
        width: 250px; /* Increased width */
        height: 60px; /* Increased height */
        font-size: 18px; /* Increased font size */
        border-radius: 8px; /* Optional: Rounded corners */
    }
    div.stButton > button:hover {
        background-color: #0056b3;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )


# Login Page
elif st.session_state.page == "login_as_user":
    login_as_user()


elif st.session_state.page == "login_as_admin":
    login_as_admin()

# Register Page
elif st.session_state.page == "register":
    register_page()
# Post-Login Page
elif st.session_state.page == "post_login":
    post_login_page()

# Health Policy Assistant Page
elif st.session_state.page == "health_policy":
    health_policy_page()

# Disease Query Page
elif st.session_state.page == "disease_query":
    disease_query_page()

# # General Query Page
# elif st.session_state.page == "general_query":
#     general_query_page()

# Prescription Page
elif st.session_state.page == "prescription":
    prescription_page()

# Language Selection Page
elif st.session_state.page == "language_selection":
    language_selection_page()

elif st.session_state.page == "admin_dashboard":
    admin_dashboard_page()

# Dashboard Page
elif st.session_state.page == "dashboard":
    dashboard_page()  # Navigate to the dashboard