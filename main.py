import os
from fastapi import FastAPI
import requests

app = FastAPI()

# Get API Keys from GitHub Secrets
DALL_E_API_KEY = os.getenv("OPENAI_API_KEY")
RUNWAYML_API_KEY = os.getenv("RUNWAYML_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

@app.get("/")
def home():
    return {"message": "FaxVidz API is running!"}

@app.get("/generate-image")
def generate_image(prompt: str):
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {DALL_E_API_KEY}"},
        json={"model": "dall-e-2", "prompt": prompt, "n": 1}
    )
    return response.json()

@app.get("/generate-video")
def generate_video(prompt: str):
    response = requests.post(
        "https://api.runwayml.com/v1/generate-video",
        headers={"Authorization": f"Bearer {RUNWAYML_API_KEY}"},
        json={"prompt": prompt}
    )
    return response.json()

@app.get("/generate-voice")
def generate_voice(text: str):
    response = requests.post(
        "https://api.elevenlabs.io/v1/text-to-speech",
        headers={"Authorization": f"Bearer {ELEVENLABS_API_KEY}"},
        json={"text": text}
    )
    return response.json()
