import os

class Config:
    MODEL_NAME = "openai/gpt-oss-120b"
    TEMPERATURE = 0.7
    API_KEY = os.getenv("GROQ_API_KEY")