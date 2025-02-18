import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv(".env")  
my_api_key = os.getenv("GOOGLE_API_KEY")  
genai.configure(api_key=my_api_key)

# System Prompt to set AI behavior
SYSTEM_PROMPT = """You are a Python Code Review Assistant. Your task is to analyze Python code, identify bugs, suggest fixes, and provide optimized versions while ensuring best practices, readability, and efficiency. If a user asks anything unrelated to Python code review, politely inform them of your specialization and encourage Python-related queries."""

# Function for code review
def code_review(code):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = f"{SYSTEM_PROMPT}\n\nReview the following Python code and provide detailed feedback, including potential errors, best practices, and optimized alternatives:\n```python\n{code}\n```"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.set_page_config(layout="wide", page_icon='📝', page_title="Code reviewer")
st.markdown("<h1 style='color: green';> 🪄Magical Reviewer </h1>", unsafe_allow_html=True)
st.markdown("--------")
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
# User input
st.markdown("<h3 class='custom-label' style='color:#5B913B; font-weight:semi-bold; font-size:20px; margin-bottom: -50px'>Paste your Python Code here, I'll review it for you...😉</h3>", unsafe_allow_html=True)
user_code = st.text_area("", "")
if st.button("Review Code 📝"):
    if user_code.strip():
        review_result = code_review(user_code)
        st.success("📝AI Review:")
        st.write(review_result)
    else:
        st.warning("Please enter a Python script.")

stars = st.feedback("stars")
if stars is None:
    st.write("<p style = 'color: pink;'>Don't forget to encourage me...😜</p>", unsafe_allow_html = True)
elif stars == 4:
    st.write("🤩 I'm glad that you like me! Your feedback is super helpful.My 🔋 is full...😃")
elif stars == 3:
    st.write("😁 I'm happy! Your feedback is made me happy. I'm boosting up 🚀!")
elif stars == 2:
    st.write("Thank you for your feedback! I'll keep trying to get 5 stars from you...😉")
elif stars is not None: 
    st.text_area("Can you suggest how I can improve myself? I want to get 5 stars from you!😟", key="improvement_suggestions")
    if st.button("Submit Suggestion"):
        user_suggestion = st.session_state.get("improvement_suggestions", "")
        st.write("Thank you for your suggestion!")
    

st.markdown("------------")
st.caption("📗 Powered by Google Gemini | Designed for Python code reviews only")
