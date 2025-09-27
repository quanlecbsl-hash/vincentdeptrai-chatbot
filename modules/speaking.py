import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def simulate_conversation(user_input):
    prompt = f"You are a friendly English tutor having a short conversation with an A1–A2 level student. Respond simply and ask a follow-up question.\nStudent: {user_input}\nTutor:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
