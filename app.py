import os
import json
from dotenv import load_dotenv
import streamlit as st
from google import genai

# Load environment variables
load_dotenv()

# Initialize the Gemini Client (Make sure you are using the new google-genai SDK)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Page Setup
st.set_page_config(page_title="AI Interview Coach", page_icon="🎤", layout="centered")

st.title("🎤 AI Interview Coach")
st.write("Paste a job description, get tailored interview questions, and receive instant AI feedback on your answers.")

st.divider()

# 1. UI Inputs
st.subheader("📋 Step 1: Provide Context")
job_description = st.text_area(
    "Paste the Job Description (JD) here:", 
    placeholder="Looking for a Data Analyst proficient in Python, SQL...",
    height=150
)

# 2. State Management for Questions
if "current_question" not in st.session_state:
    st.session_state.current_question = ""

# Button to generate a question
if st.button("✨ Generate Interview Question", type="primary"):
    if job_description.strip() == "":
        st.warning("Please paste a job description first!")
    else:
        with st.spinner("Analyzing JD and crafting a tailored question..."):
            try:
                # Call Gemini API 
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Based on this job description, generate ONE highly relevant technical or behavioral interview question: {job_description}"
                )
                st.session_state.current_question = response.text
            except Exception as e:
                st.error(f"API Error: {e}")

# 3. Display Question & Answer Box
if st.session_state.current_question:
    st.subheader("❓ Current Question")
    st.info(st.session_state.current_question)
    
    st.subheader("✏️ Step 2: Your Answer")
    user_answer = st.text_area("Type your response here:", placeholder="In my previous role, I...", height=150)
    
    # Button to evaluate the answer
    if st.button("📊 Evaluate Answer"):
        if user_answer.strip() == "":
            st.warning("Please type an answer before submitting for evaluation.")
        else:
            with st.spinner("Analyzing your response..."):
                try:
                    eval_prompt = f"""
                    You are an expert tech interviewer. 
                    Question asked: {st.session_state.current_question}
                    Candidate's Answer: {user_answer}
                    
                    Provide a constructive evaluation. Highlight strengths, weaknesses, and a concrete suggestion for improvement.
                    """
                    eval_response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=eval_prompt
                    )
                    st.subheader("💡 AI Feedback")
                    st.success(eval_response.text)
                except Exception as e:
                    st.error(f"API Error during evaluation: {e}")