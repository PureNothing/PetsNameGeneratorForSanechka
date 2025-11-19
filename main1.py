from langchain_groq import ChatGroq
from dotenv import load_dotenv
from cfg import Config

load_dotenv()

llm = ChatGroq(
    model=Config.MODEL_NAME,      
    temperature=Config.TEMPERATURE, 
    api_key=Config.API_KEY     
)
    

def generate_pet_name():

    response = llm.invoke(
        "У меня домашняя собака и я хочу крутые имена для неё. Составь пять крутых имён."
    )

    return response


if __name__ == "__main__":
    print(generate_pet_name())

# Файл .env и я сделал .gitignore там была одна срочка такого типа: GROQ_API_KEY="Апи ключ грока с их сайта без кавычек"
# Папчку .venv я тоже загитигнорил, по совету гпт