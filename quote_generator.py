import os
import cohere
import spacy
import random
from dotenv import load_dotenv

# Load environment variable
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
co = cohere.Client(COHERE_API_KEY)

# Extract keywords from caption
def extract_keywords(text):
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    return nouns[:3], adjectives[:3]

# Generate quotes using Cohere
def generate_quotes(caption, num=5):
    nouns, adjectives = extract_keywords(caption)
    keywords = nouns + adjectives
    if not keywords:
        keywords = ["vibe", "cool"]

    prompt = (
        f"Give me {num} different Gen-Z-style Instagram captions using these words: "
        f"{', '.join(keywords)}. Keep each caption under 10 words and make sure they are all different, aesthetic, fun, and trendy."
    )

    try:
        response = co.generate(
            model='command-light',
            prompt=prompt,
            max_tokens=150,
            temperature=0.9,
            k=50,
            p=0.95,
            stop_sequences=["--"],
            return_likelihoods='NONE'
        )

        # Clean and format output
        generations = response.generations[0].text.strip().split("\n")
        quotes = [quote.strip("•- \n") for quote in generations if len(quote.strip()) > 3]
        quotes = list(dict.fromkeys(quotes))  # Remove duplicates

        # Fallback if not enough captions
        if len(quotes) < num:
            fallback = [
                "Too lit to quit 🔥", "Mood = 100 ✨", "Main character energy 🎬",
                "Vibes don't lie 😎", "Drippin’ with style 💧"
            ]
            quotes += random.sample(fallback, num - len(quotes))

        return quotes[:num]

    except Exception as e:
        print("Error generating captions with Cohere:", e)
        return [
            "Default vibe 1 💫",
            "Default vibe 2 🔥",
            "Default vibe 3 😎",
            "Default vibe 4 ✨",
            "Default vibe 5 💅"
        ]
