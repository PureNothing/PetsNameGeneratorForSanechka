# Строка 1: Импортируем нужные библиотеки
import os
from groq import Groq
from dotenv import load_dotenv

# Строка 2: Загружаем переменные из .env файла
load_dotenv()

# Строка 3: Создаём клиент для работы с Groq API
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Строка 4: Пробуем отправить запрос к API
try:
    # Строка 5: Создаём запрос на генерацию текста
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "Привет! Ответь просто 'Тест пройден'"}],
        model="llama3-8b-8192",
        temperature=0.7
    )
    # Строка 6: Если успешно - печатаем ответ
    print("✅ УСПЕХ! Ответ:", chat_completion.choices[0].message.content)
except Exception as e:
    # Строка 7: Если ошибка - печатаем её
    print("❌ ОШИБКА:", e)