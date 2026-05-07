# Smart ATS Resume Analyzer

A Streamlit-based resume evaluation tool that uses Google Gemini generative AI to compare a resume PDF with a job description and provide:

- ATS match percentage
- Missing keywords
- Profile summary and improvement suggestions

## Files

- `main.py` - primary Streamlit application entrypoint
- `helper.py` - contains PDF extraction, prompt generation, and Gemini response handling
- `back.jpg` - optional background image file
- `requirements.txt` - Python package dependencies
- `required.txt` - legacy dependency list
- `.gitignore` - ignores local environment files, virtualenv, and caches

## Setup

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your Google API key:
   ```text
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Run

```bash
streamlit run main.py
```

Then open the Streamlit URL shown in the console.

## Notes

- The app requires a valid `GOOGLE_API_KEY` for the `google.generativeai` library.
- `.env` and `venv/` are excluded from git by `.gitignore`.
- No API keys or private environment files are included in this repository.
