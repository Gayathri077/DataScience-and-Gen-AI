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
st.markdown("<h1 style='color: green';> 🪄Magical Reviewer </h1>", unsafe_allow_html=True)

#styling
st.markdown(
    """
    <style>
        div.stButton > button {
            background-color:#3D8D7A; 
            color: white;
            font-size: 18px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom CSS for label text
st.markdown(
    """
    <style>
        /* Targeting the label of the text area */
        div[data-testid="stTextArea"] label {
            color: #5B913B ; 
            font-size: 25px ; 
            font-weight: bold ; 
        }
    </style>
    """,
    unsafe_allow_html=True
)

# User input
user_code = st.text_area("Submit your python code here, I'll review it for you...😉 ")
if st.button("Review Code 📝"):
    if user_code.strip():
        review_result = code_review(user_code)
        st.success("📝AI Review:")
        st.write(review_result)
    else:
        st.warning("Please enter a valid Python script.")

stars = st.feedback("stars")
st.balloons()
if stars == 4:
    st.write("🤩 Great job! Your feedback is super helpful and accurate. Keep it up!")
elif stars == 3:
    st.write("👍 Good job! Your feedback is mostly helpful and accurate. Keep improving!")
elif stars == 2:
    st.write("Thank you for your feedback! I'll keep trying to get 5 stars from you...😉")
elif stars is not None:  # Handle cases where a rating is selected
    st.text_area("Can you suggest how I can improve my feedback? I want to get 5 stars from you!", key="improvement_suggestions")
    if st.button("Submit Suggestion"):
        user_suggestion = st.session_state.get("improvement_suggestions", "")
        # ... Process the user_suggestion, e.g., save to a file or database ...
        st.write("Thank you for your suggestion!")
    

st.markdown("------------")
st.caption("💜 Powered by Google Gemini | Designed for Python code reviews only")
