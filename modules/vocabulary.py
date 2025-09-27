import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quiz(topic):
    prompt = f"Create a 3-question multiple choice vocabulary quiz for A1–A2 level learners about {topic}. Include answers and explanations."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
