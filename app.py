import streamlit as st
from chains.email_chain import generate_email
from chains.summary_chain import generate_summary
from chains.rewrite_chain import generate_rewrite
from chains.extraction_chain import extract_employee_info

st.title("AI-Powered content Assistant")
st.write("Welcome! Your AI assistant helps you generate emails, summarize text, rewrite content, and extract information.")

st.sidebar.title("Navigation")

selected_option = st.sidebar.radio(
    "Choose a feature:",
    [
        "Email Generation",
        "Text Summarization",
        "Text Rewriting",
        "Information Extraction"
    ]
)

st.write("You selected:", selected_option)

if selected_option == "Email Generation":
    st.header("Email Generation")
    recipient = st.text_input("Recipient:")
    purpose = st.text_area("Purpose:")
    details = st.text_area("Important Details:")
    tone = st.selectbox("Tone:", ["Professional", "Friendly", "Formal", "Casual"])

    if st.button("Generate Email"):
        try:
            email_content = generate_email(recipient, purpose, details, tone)
            st.subheader("Generated Email:")
            st.write(email_content)
        except Exception as e:
            st.error(f"Error: {e}")

elif selected_option == "Text Summarization":
    st.header("Text Summarization")
    text_to_summarize = st.text_area("Enter text to summarize:")

    if st.button("Generate Summary"):
        try:
            summary = generate_summary(text, summary_length)
            st.subheader("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {e}")
elif selected_option == "Text Rewriting":
    st.header("Text Rewriting")
    original_text = st.text_area("Enter text to rewrite:")
    rewrite_tone = st.selectbox("Select tone for rewriting:", ["Professional", "Friendly", "Formal", "Casual"])

    if st.button("Generate Rewrite"):
        try:
            rewritten_text = generate_rewrite(original_text, rewrite_tone)
            st.subheader("Rewritten Text:")
            st.write(rewritten_text)
        except Exception as e:
            st.error(f"Error: {e}")
elif selected_option == "Information Extraction":
    st.header("Information Extraction")
    text_for_extraction = st.text_area("Enter text for information extraction:")

    if st.button("Extract Information"):
        try:
            extracted_info = extract_employee_info(text_for_extraction)
            st.subheader("Extracted Information:")
            st.write(extracted_info)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.write("Please select a feature from the sidebar to get started.")