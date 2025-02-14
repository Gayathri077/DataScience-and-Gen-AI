import streamlit as st
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="AIzaSyA6V0AV1Z7-A7DDBJn1ne2RHehj4-nXNGg")

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
            font-size: 50px ; 
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
        st.warning("Please enter a Python script.")

stars = st.feedback("stars")
if stars is None:
    st.write("Please rate the code review...🧙🏻😟")
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
