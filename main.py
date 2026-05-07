import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re  # Import regex for extracting JSON

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini AI response
def get_gemini_response(resume_text, jd_text):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    # Strictly instructing Gemini to return JSON only
    formatted_prompt = f"""
    You are a highly accurate ATS (Applicant Tracking System).
    
    **Task:** Analyze the given resume against the job description and provide:
    - JD Match percentage
    - List of missing keywords
    - Profile summary

    **Return the result in pure JSON format without extra text**:
    ```
    {{
        "JD Match": "XX%",
        "MissingKeywords": ["keyword1", "keyword2"],
        "Profile Summary": "..."
    }}
    ```

    **Resume:** {resume_text}
    **Job Description:** {jd_text}
    """

    response = model.generate_content(formatted_prompt)
    return response.text  # Get AI-generated response as text

# Function to extract text from uploaded PDF
def extract_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page_text = reader.pages[page].extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

# Function to extract JSON safely using regex
def extract_json(text):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)  # Extract JSON-like content
        if match:
            return json.loads(match.group())  # Parse JSON safely
    except json.JSONDecodeError:
        return None  # Return None if parsing fails
    return None

# Streamlit UI
st.title("📄 Smart ATS - Resume Analyzer")
st.write("🔍 Improve your resume for better ATS matching.")

# Input fields for Job Description and Resume Upload
jd_text = st.text_area("📌 Paste the Job Description", height=150)
uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type="pdf")

# Submit button
if st.button("🚀 Analyze Resume"):
    if uploaded_file is not None:
        # Extract text from uploaded PDF
        resume_text = extract_pdf_text(uploaded_file)

        if resume_text:
            # Get AI response
            ai_response = get_gemini_response(resume_text, jd_text)

            # Extract JSON safely
            parsed_response = extract_json(ai_response)

            # Display AI response
            if parsed_response:
                st.subheader("✅ ATS Analysis Results")
                st.write(f"**🔹 JD Match:** {parsed_response['JD Match']}")
                st.write(f"**🔹 Missing Keywords:** {', '.join(parsed_response['MissingKeywords']) if parsed_response['MissingKeywords'] else 'None'}")
                st.write(f"**📌 Profile Summary:** {parsed_response['Profile Summary']}")
            else:
                st.error("❌ Error: Unable to parse the response. Gemini did not return valid JSON.")
                st.text("Raw Response from AI:")
                st.code(ai_response)  # Show raw response for debugging
        else:
            st.error("❌ Error: Could not extract text from the uploaded PDF.")
    else:
        st.warning("⚠️ Please upload your resume (PDF) first!")
