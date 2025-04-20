import streamlit as st
import plotly.express as px
import pandas as pd

def dashboard_page():
    # Center the title at the top
    st.markdown("<h1 style='text-align: center;'>AarogyaMitra AI Dashboard</h1>", unsafe_allow_html=True)

    # Placeholder for the dashboard content
    st.write("This is the dashboard page.")
    # Set the page configuration
    # st.set_page_config(page_title="AarogyaMitra AI Dashboard", layout="wide")

    # Title and header
    st.title("📊 AarogyaMitra AI Performance Dashboard")
    st.subheader("Hackathon Metrics Overview")

    # Sample metrics (replace with real data during integration)
    user_interactions = 1280
    successful_claims = 320
    language_usage = {
        "Hindi": 540,
        "Bengali": 280,
        "Tamil": 140,
        "Others": 320
    }
    symptom_mapping_success = 75  # in %

    # Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("User Interactions", f"{user_interactions}", "+18%")
    col2.metric("Successful Claim Assistance", f"{successful_claims}", "+22%")
    col3.metric("Languages Used", f"{len(language_usage)}", "⬆️")
    col4.metric("Symptom Mapping Accuracy", f"{symptom_mapping_success}%", "✅")

    # Section: Language Usage Chart
    st.markdown("### 🌐 Language Support Utilization")
    lang_df = pd.DataFrame({
        "Language": list(language_usage.keys()),
        "Users": list(language_usage.values())
    })
    fig_lang = px.pie(lang_df, names="Language", values="Users", title="Voice & Language Usage")
    st.plotly_chart(fig_lang, use_container_width=True)

    # Section: Claim Filing Trend (Sample)
    st.markdown("### 📁 Claim Filing Assistance Over Time")
    claim_data = pd.DataFrame({
        "Date": pd.date_range(start="2024-06-01", periods=10),
        "Claims Assisted": [12, 25, 40, 58, 68, 70, 85, 95, 105, 120]
    })
    fig_trend = px.line(claim_data, x="Date", y="Claims Assisted", markers=True, title="Claim Assistance Trend")
    st.plotly_chart(fig_trend, use_container_width=True)

    # Feedback Score (placeholder)
    st.markdown("### 📝 User Feedback (Simulated)")
    feedback_score = 4.2  # out of 5
    st.progress(feedback_score / 5)
    st.success(f"Average Feedback: {feedback_score} / 5")

    # Footer
    st.markdown("---")
    st.caption("© 2025 AarogyaMitra AI | Powered by GenAI | Hackathon Edition")
    if st.button("Back to previous_page"):
        st.session_state.page = "admin_dashboard"  # Navigate back to Main Page
