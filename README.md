Of course! Here’s a professional README.md for your Flask project based on the code you shared:

I’ll keep it clean, detailed, and ready for GitHub 👇

⸻

🎵🖼️ Caption Beat - AI-Powered Image Caption & Music Recommendation App

Caption Beat is a Flask web app where users can upload an image, input a mood or custom text, and receive:
	•	A descriptive image caption generated using a BLIP model,
	•	Five unique Gen Z–style captions,
	•	A curated list of Spotify song suggestions matching the mood or theme.

⸻

🚀 Features
	•	📸 AI Image Captioning: Upload any image and get an automatic description (using BLIP model).
	•	✨ Gen Z–style Caption Generation: Generate trendy, catchy captions from the image description (using spaCy + HuggingFace).
	•	🎶 Spotify Song Recommendations: Get personalized song suggestions based on your mood or custom keywords.
	•	📂 Image Upload and Preview: View your uploaded image on the results page.
	•	🎨 Pastel-themed Frontend: Clean, soft, and modern UI.

⸻

🛠️ Tech Stack
	•	Backend: Flask (Python)
	•	Frontend: HTML, CSS (with pastel UI)
	•	AI Models:
	•	BLIP for image captioning
	•	spaCy + Hugging Face models for quote generation
	•	Music API: Spotify Web API (Spotipy)
	•	Utilities: python-dotenv (for managing API credentials)

⸻

📂 Project Structure

Caption-Beat/
├── static/
│   └── uploads/       # Uploaded images
├── templates/
│   └── index.html      # Main frontend template
├── .env                # Environment variables (Spotify API keys)
├── app.py              # Main Flask application (your shared code)
├── blip_caption.py     # BLIP model logic for image caption generation
├── quote_generator.py  # spaCy + HuggingFace logic for Gen-Z captions
├── README.md           # (this file)
├── requirements.txt    # Python dependencies



⸻

⚙️ Installation Guide

1. Clone the Repository

git clone https://github.com/your-username/Caption-Beat.git
cd Caption-Beat

2. Create a Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Requirements

pip install -r requirements.txt

4. Set up Environment Variables

Create a .env file in the root directory and add:

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

⚡ You can get Spotify credentials by creating an app at Spotify Developer Dashboard.

5. Run the App

python app.py

	•	The app will run on http://127.0.0.1:5001.

⸻

🧠 How it Works
	1.	User Uploads Image ➔
→ generate_image_caption(filepath) generates a descriptive caption.
	2.	Image Caption to Gen Z Captions ➔
→ generate_quotes(image_caption, num=5) produces 5 trendy caption suggestions.
	3.	User Inputs Mood or Text ➔
→ get_suggestions(user_input) fetches 5 matching songs from Spotify.
	4.	Result Page ➔
→ Displays uploaded image, AI-generated captions, and Spotify music embeds.

⸻

🧩 Dependencies
	•	Flask
	•	Spotipy
	•	spaCy
	•	Cohere 
	•	dotenv
	•	torch (for BLIP model)
	•	PIL (Pillow for image handling)

⸻

Feel free to contribute by opening a Pull Request or raising an Issue!
