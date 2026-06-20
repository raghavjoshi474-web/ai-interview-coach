# 🎤 AI Interview Coach

An AI-powered interview preparation tool that generates tailored interview questions from any job description and provides expert-level feedback on your answers — built using Google's Gemini API.

**🔗 Live App:** [ai-interview-coach-suhktbjnnhhv7wsgtnn3vn.streamlit.app](https://ai-interview-coach-suhktbjnnhhv7wsgtnn3vn.streamlit.app)

## Problem Statement
Generic interview prep resources don't adapt to the specific role you're applying for. This tool analyzes a real job description, generates a relevant question, and evaluates your answer the way an experienced technical interviewer would — highlighting strengths, gaps, and a stronger model answer.

## How It Works
1. Paste any job description
2. AI generates a tailored interview question based on the specific skills mentioned
3. Type your answer
4. AI evaluates your response with structured feedback: strengths, areas to improve, and a suggested stronger answer

## What I Built
- Integrated Google's Gemini API (`google-genai` SDK) for question generation and answer evaluation
- Designed prompts to extract structured, evaluator-style feedback rather than generic responses
- Implemented structured JSON output parsing for consistent, scorable feedback
- Built a full interactive web interface using Streamlit with session state management
- Deployed live on Streamlit Community Cloud with secure API key handling via secrets management

## Example Output
**Input Job Description:** "Looking for a Data Scientist with Python, SQL, and machine learning experience"

**Generated Question:** "Tell me about a machine learning project you worked on that you're particularly proud of. Walk me through it from start to finish..."

**AI Feedback includes:**
- Specific strengths in the response
- Concrete gaps (e.g., missing technical depth, unclear business impact)
- A rewritten example answer using the STAR framework

## Technologies Used
Python | Streamlit | Google Gemini API (`google-genai`) | python-dotenv | Prompt Engineering | JSON Structured Output

## Key Learning
Building this project required moving beyond simple prompt-response patterns into **prompt engineering for structured, evaluative output** — getting an LLM to act as a consistent, rigorous evaluator rather than a generic assistant. This is a foundational skill for building real GenAI products.
