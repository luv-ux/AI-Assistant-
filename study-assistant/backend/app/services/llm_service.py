import os
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)

SYSTEM_PROMPT = """You are a study assistant, explain topics simply,
                always give examples"""

def get_ai_response(user_message , conversation_history = None):

    if conversation_history is None:
        conversation_history = []

    messages = conversation_history + [
        {"role" : "user" , "content" : user_message}
    ]

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=messages
        )

        reply = response.content[0].text
        return reply

    except Exception as e:
        return f"Error:{str(e)}"

