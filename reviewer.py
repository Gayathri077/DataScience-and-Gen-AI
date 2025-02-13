import streamlit as st
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="AIzaSyA6V0AV1Z7-A7DDBJn1ne2RHehj4-nXNGg")

# System Prompt to set AI behavior
SYSTEM_PROMPT = """You are a Python code review assistant. Users will submit Python code snippets, and you will provide feedback on potential bugs, suggest fixes, and offer optimized code snippets.
If a user asks a question unrelated to Python code review, politely explain that you are designed specifically for Python code analysis and cannot assist with other types of queries.
Encourage them to ask questions related to Python code."""

# Function to check if input is valid Python code
def is_valid_python_code(code):
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        return False

# Function for code review
def code_review(code):
    if not is_valid_python_code(code):
        return "⚠️ This tool only reviews Python code. Please submit a valid Python script."
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = f"{SYSTEM_PROMPT}\n\nReview the following Python code and provide detailed feedback, including potential errors, best practices, and optimized alternatives:\n```python\n{code}\n```"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("🐍 Code Reviewer")
st.write("Submit your **Python** code, and I'll review it for you!😉")

# User input
user_code = st.text_area("Paste your Python code here:")

if st.button("Review Code"):
    if user_code.strip():
        review_result = code_review(user_code)
        st.success("📝AI Review:")
        st.write(review_result)
    else:
        st.warning("Please enter a valid Python script.")

st.markdown("------------")
st.caption("💜 Powered by Google Gemini | Designed for Python code reviews only")
