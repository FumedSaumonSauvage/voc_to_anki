import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class ModelLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
            cls._instance.client = genai.Client()
            cls._instance.model_name = os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")
        return cls._instance
