# Smart ATS Resume Analyzer Report

## Project Summary

This repository contains a resume-analyzer application built using Streamlit and Google Gemini's generative AI. The app compares a PDF resume with a job description and returns structured ATS feedback.

## Objectives

- Extract text from a resume PDF
- Compare resume content against a job description
- Generate a match percentage, missing keywords, and a profile summary
- Present results to users in a simple Streamlit web interface

## Components

- `main.py`: The main Streamlit application with UI controls and workflow logic.
- `helper.py`: Utility functions for configuring Gemini, extracting PDF text, prompt construction, and response validation.
- `back.jpg`: Optional background image asset.
- `requirements.txt`: Standard dependency file for Python package installation.
- `README.md`: Setup and usage instructions.
- `.gitignore`: Files and directories excluded from git.

## Dependencies

The key dependencies are:

- `streamlit`
- `google.generativeai`
- `PyPDF2`
- `python-dotenv`
- `streamlit_extras`

## Known Limitations

- The app relies on the user providing a valid Google API key.
- Resume extraction is based on PDF text extraction and may fail on scanned or image-only PDFs.
- The output quality depends on the Gemini model's interpretation of the prompt.

## Deployment Instructions

1. Clone the repository.
2. Create a virtual environment and install dependencies.
3. Set `GOOGLE_API_KEY` in `.env` or the environment.
4. Run `streamlit run main.py`.

## Recommended Improvements

- Add error handling for missing or invalid API keys.
- Support DOCX/resume formats in addition to PDF.
- Improve prompt validation and response parsing for more robust JSON handling.
