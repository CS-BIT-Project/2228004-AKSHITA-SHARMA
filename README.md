# 🎵 CaptionBeat – AI-Powered Instagram Caption & Song Suggestion Generator

<img src="https://cdn-icons-png.flaticon.com/512/7281/7281890.png" width="120" align="right"/>

> ✨ *Turn Your Vibes into Captions & Beats*  
> **CaptionBeat** is a fun and creative AI web app that generates aesthetic captions and song recommendations based on the image, mood, and keywords you provide.

---

## 🔍 About the Project

**CaptionBeat** uses computer vision (BLIP) to analyze images and generate captions, then enhances them using NLP techniques (spaCy + Hugging Face). It also fetches curated songs from Spotify based on your mood or keywords.

🌸 Built with a soft pastel-themed UI using **TailwindCSS + HTML + JS**  
🧠 AI-generated captions & Gen-Z style suggestions  
🎶 Real-time song recommendations via **Spotify API**

---

## ✨ Features

- 📸 Upload an image with drag & drop or file picker
- 🧠 AI-generated image captions using **BLIP**
- ✨ Gen-Z aesthetic caption suggestions (using spaCy + HuggingFace)
- 🎵 Spotify song recommendations based on mood or keywords
- 🎨 Modern responsive frontend with **TailwindCSS**
- 💡 Easy-to-use interface with preview and animations

---

## 🛠️ Tech Stack

| Layer        | Tools & Libraries |
|--------------|-------------------|
| **Frontend** | HTML5, TailwindCSS, JavaScript |
| **Backend**  | Python, Flask |
| **ML Models**| BLIP (Image Captioning), spaCy, Hugging Face Transformers |
| **APIs**     | Spotipy (Spotify Web API) |
| **Deployment** | Localhost (Flask dev server) |

---

## 📂 Folder StructureCaptionBeat/
│
├── static/                   
│
├── templates/
│   └── try.html               
├── main_.py                    
├── blip_caption.py            
├── quote_generator.py          
├── requirements.txt            
└── README.md                  
---

## 🚀 How to Run the Project

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/CaptionBeat.git
cd CaptionBeat

2.	Install dependencies
pip install -r requirements.txt

3.	Set up environment variables
Create a .env file
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret

4.	Run the app
python main.py
