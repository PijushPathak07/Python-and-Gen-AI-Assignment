from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in environment variables")
    MAX_TOKENS = 20000
    MODEL_NAME = "gemini-1.5-flash"