
from flask import Flask, render_template, request
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from blip_caption import generate_image_caption  # BLIP caption
from quote_generator import generate_quotes  # spaCy + HuggingFace
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))


def get_suggestions(user_input):
    """Fetch Spotify song suggestions based on user mood or input."""
    if not user_input:
        user_input = "happy"

    user_input = user_input.lower()

    # Mood to Spotify query mapping
    mood_to_query = {
        "happy": "bollywood upbeat OR hollywood pop OR punjabi bhangra",
        "sad": "bollywood sad songs OR hollywood acoustic OR punjabi emotional",
        "chill": "chill bollywood OR chill hollywood OR chill punjabi lo-fi",
        "romantic": "bollywood love songs OR hollywood romance OR punjabi romantic hits",
        "energetic": "bollywood dance OR hollywood workout beats OR punjabi party anthems",
        "heartbreak": "bollywood breakup OR hollywood heartbreak OR punjabi sad love",
        "motivated": "motivational bollywood OR gym hollywood OR punjabi hype songs",
        "angry": "hollywood metal OR bollywood intense beats OR punjabi aggressive rap",
        "nostalgic": "old bollywood classics OR 2000s hollywood hits OR retro punjabi",
        "aesthetic": "aesthetic lo-fi bollywood OR aesthetic pop OR dreamy punjabi vibes",

        # Additional popular moods
        "party": "punjabi bhangra OR bollywood party mix OR hollywood edm",
        "focus": "bollywood instrumental focus OR hollywood ambient OR punjabi chill",
        "lofi": "lofi bollywood OR lo-fi chillhop OR punjabi lo-fi beats",
        "funny": "funny bollywood songs OR meme hollywood tracks OR quirky punjabi",
        "roadtrip": "bollywood roadtrip OR hollywood driving songs OR punjabi travel vibes",
        "study": "bollywood soft focus OR hollywood study beats OR punjabi chill study",
    }

    # Use mood-specific query or fallback to input
    search_query = mood_to_query.get(user_input, user_input)

    suggested_songs = []

    try:
        results = sp.search(q=search_query, limit=5, type="track")
        for track in results["tracks"]["items"]:
            suggested_songs.append({
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "url": track["external_urls"]["spotify"],
                "embed": f"https://open.spotify.com/embed/track/{track['id']}"
            })
    except Exception as e:
        suggested_songs.append({
            "name": "Error fetching songs",
            "artist": "",
            "url": "#",
            "embed": "",
            "error": str(e)
        })

    return suggested_songs


@app.route("/", methods=["GET", "POST"])
def home():
    suggestions = {"songs": []}
    uploaded_image = None
    image_caption = ""
    generated_quotes = []
    user_input = ""

    if request.method == "POST":
        # Get values from form
        mood_dropdown = request.form.get("mood", "").strip()
        custom_input = request.form.get("text", "").strip()
        file = request.files.get("image")

        # Choose the more specific input
        user_input = custom_input if custom_input else mood_dropdown

        if file and file.filename:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            uploaded_image = filepath

            # Generate caption
            image_caption = generate_image_caption(filepath)

            # Generate Gen Z–style captions
            generated_quotes = generate_quotes(image_caption, num=5)

        if user_input:
            suggestions["songs"] = get_suggestions(user_input)

    return render_template("hlo.html",
                           suggestions=suggestions,
                           uploaded_image=uploaded_image,
                           user_input=user_input,
                           image_caption=image_caption,
                           generated_quotes=generated_quotes)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
