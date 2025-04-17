from google import genai
import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path="C:/Users/ronis/OneDrive - Global College of Management/sumarizer/.env"
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def summarizerAI(name):
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=[f"Give me the summarry of the book {name}"]
    )
    print(response.text)
