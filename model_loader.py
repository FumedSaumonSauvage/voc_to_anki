import os
from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

class ModelLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
            api_key = os.getenv("MISTRAL_API_KEY")
            cls._instance.model_name = os.getenv("MISTRAL_MODEL", "mistral-large-latest")
            cls._instance.client = Mistral(api_key=api_key)
        return cls._instance