import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = "openai/gpt-oss-120b"
    TEMPERATURE = 0.7
    API_KEY = os.getenv("API_KEY_GROK")