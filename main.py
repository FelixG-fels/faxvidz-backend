import os
from fastapi import FastAPI
import requests

app = FastAPI()

# Get API Keys from Environment Variables
DALL_E_API_KEY = os.getenv("OPENAI_API_KEY")
RUNWAYML_API_KEY = os.getenv("RUNWAYML_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

@app.get("/generate-image")
def generate_image(prompt: str):
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {DALL_E_API_KEY}"},
        json={"model": "dall-e-2", "prompt": prompt, "n": 1}
    )
    return response.json()
