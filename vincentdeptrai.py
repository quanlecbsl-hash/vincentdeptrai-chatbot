import streamlit as st
from modules.grammar import correct_grammar
from modules.vocabulary import generate_quiz
from modules.writing import writing_prompt
from modules.listening import speak_text
from modules.speaking import simulate_conversation
from modules.exercise import generate_exercise

st.set_page_config(page_title="Vincentdeptrai", page_icon="🧠")
st.title("🧠 Vincentdeptrai: English Practice (A1–A2)")

mode = st.selectbox("Choose a mode:", [
    "Grammar Correction",
    "Vocabulary Quiz",
    "Writing Practice",
    "Listening Practice",
    "Speaking Practice",
    "Grammar Exercise"
])

if mode == "Grammar Correction":
    sentence = st.text_input("Enter a sentence:")
    if sentence:
        st.write(correct_grammar(sentence))

elif mode == "Vocabulary Quiz":
    topic = st.text_input("Enter a topic (e.g., food, animals):")
    if topic:
        st.write(generate_quiz(topic))

elif mode == "Writing Practice":
    theme = st.text_input("Choose a theme (e.g., daily routine):")
    if theme:
        st.write(writing_prompt(theme))

elif mode == "Listening Practice":
    text = st.text_input("Enter a sentence to hear:")
    if text:
        speak_text(text)

elif mode == "Speaking Practice":
    user_input = st.text_input("Say something in English:")
    if user_input:
        st.write(simulate_conversation(user_input))

elif mode == "Grammar Exercise":
    topic = st.text_input("Enter a grammar topic (e.g., present simple):")
    if topic:
        st.write(generate_exercise(topic))
