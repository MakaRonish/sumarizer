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
        model="gemini-2.0-flash",
        contents=[
            f"Summarize the book {name} .I want a detailed yet concise summary that includes: The main plot or narrative structure Key characters and their development Major themes and messages Important events or turning points The author's purpose or style (if relevant) Please keep the summary engaging and easy to understand, like explaining it to someone who hasn’t read the book but wants to know what it’s about and why it matters.Also write in proper format like the space paragraph and all dont use unnecesarry symbols make it as professional and write atleast 1500 words"
        ],
    )
    summarry = response.text
    return summarry
