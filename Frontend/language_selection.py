import streamlit as st

def language_selection_page():
    # Center the title at the top
    st.markdown("<h1 style='text-align: center;'>Select Your Language</h1>", unsafe_allow_html=True)

    # Language selection dropdown
    language = st.selectbox("Choose your preferred language:", ["English", "Hindi", "Spanish", "French", "German"])

    # Confirm button
    if st.button("Confirm"):
        st.success(f"You have selected {language} as your preferred language.")
        
    if st.button("Back to Previous page"):
        st.session_state.page = "post_login"  # Navigate back to the post-login page
    