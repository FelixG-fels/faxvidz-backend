from fastapi import FastAPI
import requests

app = FastAPI()

DALL_E_API_KEY = "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"
RUNWAYML_API_KEY = "Key_3914aec899fd440930ada481fec5d0ae961d8a4dd433b1078446aa992af2e33864397f257041008e33000b8bc1f9a47222129b6341eca02c4c71d3ac151b6d94"
ELEVENLABS_API_KEY = "Sk_888a29c792a6885d61b5c0e3df70e75eefcf09555888d2ad"

@app.get("/generate-image")
def generate_image(prompt: str):
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {DALL_E_API_KEY}"},
        json={"model": "dall-e-2", "prompt": prompt, "n": 1}
    )
    return response.json()
