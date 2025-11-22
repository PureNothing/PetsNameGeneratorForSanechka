import requests
import socket

try:
    # Пробуем получить IP адрес Groq
    ip = socket.gethostbyname("api.groq.com")
    print(f"✅ IP адрес Groq: {ip}")
    
    # Пробуем подключиться без API ключа
    response = requests.get("https://api.groq.com/openai/v1/models", timeout=10)
    print(f"✅ Статус подключения: {response.status_code}")
    
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")