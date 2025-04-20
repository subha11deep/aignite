import streamlit as st

def admin_dashboard_page():
    # Title for the admin dashboard
    st.markdown("<h1 style='text-align: center;'>Logged in as Admin</h1>", unsafe_allow_html=True)

    # Section for filling claim details
    st.markdown("<h3>Upload claim file procedure manual</h3>", unsafe_allow_html=True)

    # Input field for insurance company name
    insurance_company = st.text_input("Insurance Company Name", placeholder="Enter the insurance company name")

    # File uploader for revised claim details
    uploaded_file = st.file_uploader("Upload Revised Claim Details (PDF only):", type=["pdf"])

    # Input field for revised version number
    revised_version = st.text_area("Revised Version number", placeholder="Enter the revised version details")

    # Submit button
    if st.button("Submit"):
        if insurance_company and uploaded_file and revised_version:
            # Simulate API call or backend logic here
            st.success("Claim details submitted successfully!")
            st.write(f"Insurance Company: {insurance_company}")
            st.write(f"Uploaded File: {uploaded_file.name}")
            st.write(f"Revised Version: {revised_version}")
        else:
            st.error("Please fill in all fields and upload the required file.")
    # Button to navigate to the Dashboard
    if st.button("Go to Dashboard"):
        st.session_state.page = "dashboard"  # Set session state to navigate to the dashboard
    if st.button("Back to PREVIOUS PAGE"):
        st.session_state.page = "login_as_admin"  # Navigate back to Main Page