from google import genai
from dotenv import load_dotenv
import os

from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Configure Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def get_response(user_input, chat_history):

    try:

        # Emergency support
        if (
            "suicide" in user_input.lower()
            or "hurt myself" in user_input.lower()
        ):

            return """
I'm really sorry you're feeling this way.

Please contact a trusted person or mental health professional immediately.

You matter and support is available.
"""

        # Emotion detection
        if "stress" in user_input.lower():

            user_input += "\nUser seems stressed."

        if "sad" in user_input.lower():

            user_input += "\nUser seems emotionally low."

        # Build conversation history
        history = ""

        for msg in chat_history:

            role = msg["role"]
            content = msg["content"]

            history += f"{role}: {content}\n"

        # Final prompt
        final_prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{history}

Current User Message:
{user_input}
"""

        # Generate Gemini response
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=final_prompt
        )

        return response.text

    except Exception as e:

        # Log errors
        with open("logs.txt", "a") as file:

            file.write(f"Error: {str(e)}\n")

        # Quota exceeded handling
        if "429" in str(e):

            return """
API quota exceeded.

Please wait for a minute and try again.
"""

        return f"Error: {str(e)}"