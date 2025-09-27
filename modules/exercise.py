import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_exercise(topic):
    prompt = f"Create a grammar exercise for A1–A2 level students about '{topic}'. Include instructions, 3 questions, and answers."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
