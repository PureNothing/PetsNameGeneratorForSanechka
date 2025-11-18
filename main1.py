from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def generate_pet_name():
    llm = ChatGroq(
        model="llama3-8b",
        temperature=0.7,
        api_key=os.getenv("GROQ_API_KEY")
    )

    response = llm.invoke(
        "У меня домашняя собака и я хочу крутые имена для неё. Составь пять крутых имён."
    )

    return response

if __name__ == "__main__":
    print(generate_pet_name())

# Файл .env и я сделал .gitignore там была одна срочка такого типа: GROQ_API_KEY="Апи ключ грока с их сайта без кавычек"
# Папчку .venv я тоже загитигнорил, по совету гпт