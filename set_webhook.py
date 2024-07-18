import requests

TOKEN = '7483301543:AAF9wHD4m_B8IUMOMA9GSu0VwFXbCQTuJws'
WEBHOOK_URL = 'https://tohabastion.pythonanywhere.com/webhook/'

url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
response = requests.post(url, data={"url": WEBHOOK_URL})

if response.status_code == 200:
    print("Webhook встановлено успішно")
else:
    print(f"Не вдалося встановити webhook. Статус: {response.status_code}, Текст: {response.text}")