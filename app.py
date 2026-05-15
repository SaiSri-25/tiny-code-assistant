import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Streamlit page settings
st.set_page_config(
    page_title="Tiny Code Assistant",
    page_icon="💡",
    layout="wide"
)

# Sidebar
st.sidebar.title("Tiny Code Assistant 🚀")
st.sidebar.write("AI-powered coding helper for hackathons")

# Main title
st.title("💡 Tiny Code Assistant")

st.write(
    "Explain, Debug and Optimize Python Code using AI"
)

# Select feature
mode = st.selectbox(
    "Choose Function",
    [
        "Explain Code",
        "Debug Code",
        "Optimize Code",
        "Python Q&A"
    ]
)

# File uploader
uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

# Code input area
code_input = st.text_area(
    "Paste Python Code",
    height=300
)

# Question input
question = st.text_input(
    "Ask Python Question"
)

# Final code variable
final_code = code_input

# Read uploaded file
if uploaded_file is not None:
    final_code = uploaded_file.read().decode("utf-8")

# Create prompts
prompt = ""

if mode == "Explain Code":
    prompt = f"""
    Explain this Python code clearly in simple English.

    Code:
    {final_code}
    """

elif mode == "Debug Code":
    prompt = f"""
    Debug this Python code.

    Tasks:
    - Find errors
    - Explain errors
    - Provide corrected code

    Code:
    {final_code}
    """

elif mode == "Optimize Code":
    prompt = f"""
    Optimize and refactor this Python code.

    Tasks:
    - Improve readability
    - Improve performance
    - Follow best practices

    Code:
    {final_code}
    """

elif mode == "Python Q&A":
    prompt = f"""
    Answer this Python programming question clearly.

    Question:
    {question}
    """

# Generate response button
if st.button("Generate Response"):

    # Validation
    if mode != "Python Q&A" and final_code.strip() == "":
        st.error("Please enter or upload Python code.")

    elif mode == "Python Q&A" and question.strip() == "":
        st.error("Please enter a question.")

    else:

        with st.spinner("Generating response..."):

            try:

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                output = response.choices[0].message.content

                st.subheader("AI Response")

                st.code(output)

            except Exception as e:
                st.error(f"Error: {e}")