from fastapi import FastAPI
import requests

app = FastAPI()

DALL_E_API_KEY = "your-openai-api-key"
RUNWAYML_API_KEY = "your-runwayml-api-key"
ELEVENLABS_API_KEY = "your-elevenlabs-api-key"

@app.get("/generate-image")
def generate_image(prompt: str):
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {DALL_E_API_KEY}"},
        json={"model": "dall-e-2", "prompt": prompt, "n": 1}
    )
    return response.json()
