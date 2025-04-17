from google import genai
import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path="C:/Users/ronis/OneDrive - Global College of Management/sumarizer/.env"
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(GEMINI_API_KEY)