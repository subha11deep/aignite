# import streamlit as st
# import requests  # For API calls

# def prescription_page():
#     # Title and description
#     st.markdown("<h1 style='text-align: center;'>Prescription Assistant</h1>", unsafe_allow_html=True)
#     st.markdown(
#         "<p style='text-align: center;'>Choose an option below to analyze your prescription and check if any detected diseases are covered under your insurance.</p>",
#         unsafe_allow_html=True,
#     )

#     # Dropdown for options
#     option = st.selectbox("Select an option:", ["Choose your existing prescription", "Upload new prescription"])

#     # If user selects "Choose your existing prescription"
#     if option == "Choose your existing prescription":
#         st.write("Fetching your existing prescription details...")
#         # Call the API to fetch and analyze the existing prescription
#         try:
#             # Example API call (replace with your actual API endpoint)
#             api_url = "https://example.com/api/analyze_existing_prescription"  # Replace with your API endpoint
#             payload = {"user_id": "12345"}  # Replace with actual user ID or relevant data
#             response = requests.post(api_url, json=payload)
#             response_data = response.json()

#             # Display the API response
#             if response.status_code == 200:
#                 st.success("Prescription analysis completed!")
#                 st.write("### Analysis Results:")
#                 st.write(response_data.get("analysis", "No analysis details available."))
#             else:
#                 st.error(f"Error: {response_data.get('error', 'Unable to fetch prescription details.')}")

#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")

#     # If user selects "Upload new prescription"
#     elif option == "Upload new prescription":
#         uploaded_file = st.file_uploader("Upload your prescription (PDF only):", type=["pdf"])
#         if uploaded_file is not None:
#             st.write("Analyzing your uploaded prescription...")
#             # Call the API to analyze the uploaded prescription
#             try:
#                 # Example API call (replace with your actual API endpoint)
#                 api_url = "https://example.com/api/analyze_uploaded_prescription"  # Replace with your API endpoint
#                 files = {"file": uploaded_file.getvalue()}  # Send the uploaded file as binary data
#                 response = requests.post(api_url, files=files)
#                 response_data = response.json()

#                 # Display the API response
#                 if response.status_code == 200:
#                     st.success("Prescription analysis completed!")
#                     st.write("### Analysis Results:")
#                     st.write(response_data.get("analysis", "No analysis details available."))
#                 else:
#                     st.error(f"Error: {response_data.get('error', 'Unable to analyze the uploaded prescription.')}")

#             except Exception as e:
#                 st.error(f"An error occurred: {str(e)}")


import streamlit as st
import requests  # For API calls

def prescription_page():
    # Title and description
    st.markdown("<h1 style='text-align: center;'>Prescription Assistant</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>Choose an option below to analyze your prescription and check if any detected diseases are covered under your insurance.</p>",
        unsafe_allow_html=True,
    )

    # Dropdown for options
    option = st.selectbox("Select an option:", ["Choose your existing prescription", "Upload new prescription"])

    # If user selects "Choose your existing prescription"
    if option == "Choose your existing prescription":
        st.write("Fetching your existing prescription list...")
        try:
            # API call to fetch the list of existing prescriptions
            api_url = "https://example.com/api/get_prescriptions"  # Replace with your API endpoint
            payload = {"user_id": "12345"}  # Replace with actual user ID or relevant data
            response = requests.post(api_url, json=payload)
            response_data = response.json()

            # Check if the API call was successful
            if response.status_code == 200:
                prescription_list = response_data.get("prescriptions", [])
                if not prescription_list:
                    st.warning("No prescriptions found.")
                else:
                    # Dropdown to select a specific prescription
                    selected_prescription = st.selectbox("Select a prescription:", prescription_list)

                    if st.button("Analyze Prescription"):
                        st.write(f"Analyzing prescription: {selected_prescription}...")
                        # API call to analyze the selected prescription
                        analyze_api_url = "https://example.com/api/analyze_prescription"  # Replace with your API endpoint
                        analyze_payload = {"prescription_name": selected_prescription}
                        analyze_response = requests.post(analyze_api_url, json=analyze_payload)
                        analyze_data = analyze_response.json()

                        if analyze_response.status_code == 200:
                            st.success("Analysis completed!")
                            st.write("### Analysis Results:")
                            st.write(analyze_data.get("analysis", "No analysis details available."))
                        else:
                            st.error(f"Error: {analyze_data.get('error', 'Unable to analyze the prescription.')}")
            else:
                st.error(f"Error: {response_data.get('error', 'Unable to fetch prescription list.')}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # If user selects "Upload new prescription"
    elif option == "Upload new prescription":
        # Initialize session state for multiple uploads
        if "uploaded_prescriptions" not in st.session_state:
            st.session_state.uploaded_prescriptions = []

        # Form to upload a new prescription
        with st.form(key="upload_form"):
            uploaded_file = st.file_uploader("Upload your prescription (PDF only):", type=["pdf"])
            doctor_name = st.text_input("Enter Doctor Name:")
            appointment_date = st.date_input("Enter Appointment Date:")
            add_more = st.form_submit_button("Add More")

            if add_more:
                if uploaded_file and doctor_name and appointment_date:
                    # Add the uploaded prescription to the session state
                    st.session_state.uploaded_prescriptions.append({
                        "file": uploaded_file,
                        "doctor_name": doctor_name,
                        "appointment_date": str(appointment_date),
                    })
                    st.success("Prescription added! You can add more or submit.")
                else:
                    st.error("Please fill in all fields before adding.")

        # Display the list of uploaded prescriptions
        if st.session_state.uploaded_prescriptions:
            st.write("### Uploaded Prescriptions:")
            for idx, prescription in enumerate(st.session_state.uploaded_prescriptions):
                st.write(f"{idx + 1}. Doctor: {prescription['doctor_name']}, Date: {prescription['appointment_date']}")

        # Submit button to process all uploaded prescriptions
        if st.button("Submit All"):
            st.write("Submitting all uploaded prescriptions...")
            try:
                # API call to analyze all uploaded prescriptions
                api_url = "https://example.com/api/analyze_uploaded_prescriptions"  # Replace with your API endpoint
                files = [
                    {
                        "file": prescription["file"].getvalue(),
                        "doctor_name": prescription["doctor_name"],
                        "appointment_date": prescription["appointment_date"],
                    }
                    for prescription in st.session_state.uploaded_prescriptions
                ]
                response = requests.post(api_url, json={"prescriptions": files})
                response_data = response.json()

                if response.status_code == 200:
                    st.success("All prescriptions analyzed successfully!")
                    st.write("### Analysis Results:")
                    st.write(response_data.get("analysis", "No analysis details available."))
                else:
                    st.error(f"Error: {response_data.get('error', 'Unable to analyze the uploaded prescriptions.')}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    if st.button("Back to Main"):
        st.session_state.page = "main"  # Navigate back to Main Page