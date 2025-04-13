import os
import requests
import spacy
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    return nouns[:3], adjectives[:3]

def generate_quotes(caption, num=5):
    nouns, adjectives = extract_keywords(caption)

    if not nouns:
        nouns = ["vibes"]
    if not adjectives:
        adjectives = ["aesthetic"]

    keywords = adjectives + nouns
    prompt = (
        f"Write {num} short, stylish, aesthetic Instagram captions using these keywords: "
        + ", ".join(keywords)
        + ". Keep them under 10 words. No hashtags. No links."
    )

    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
        "parameters": {
            "temperature": 0.9,
            "max_new_tokens": 100,
            "num_return_sequences": 1,
            "return_full_text": False
        }
    })

    if response.status_code == 200:
        text_output = response.json()[0]["generated_text"]
        raw_quotes = text_output.split("\n")

        quotes = [
            q.strip() for q in raw_quotes
            if 5 < len(q.strip()) < 120 and not any(x in q for x in ["http", "@", "$"])
        ][:num]

        if len(quotes) < num:
            fallback = [
                "Main character energy 🎬",
                "Golden hour vibes only 🌅",
                "Slaying in silence 🔥",
                "Soft days, loud dreams ✨",
                "Eyes full of stars ✨"
            ]
            quotes += random.sample(fallback, num - len(quotes))

        return quotes
    else:
        print("API Error:", response.text)
        return ["Main character energy 🎬", "Slaying in silence 🔥"]

