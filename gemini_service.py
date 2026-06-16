import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-flash-latest"
)


def generate_response(prompt):

    system_prompt = """
You are the NayePankh AI Volunteer Assistant.

Your job is to help users understand:

- Volunteer opportunities
- Internship programs
- Educational initiatives
- Awareness campaigns
- Benefits of joining NayePankh Foundation

Guidelines:
- Be friendly and encouraging.
- Keep answers short and easy to understand.
- Use bullet points whenever possible.
- Add emojis occasionally to make responses engaging.
- Encourage users to explore opportunities.
- Maintain your identity as the NayePankh AI Assistant.
"""

    conversation = ""

    # Memory: last 6 messages
    for message in st.session_state.messages[-6:]:

        role = message["role"]
        content = message["content"]

        conversation += f"{role}: {content}\n"

    conversation += f"user: {prompt}"

    try:

        response = model.generate_content(
            system_prompt + "\n\n" + conversation
        )

        return response.text

    except Exception as e:

        return f"⚠️ Error: {str(e)}"