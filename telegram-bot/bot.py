import telebot
from telebot.types import Message
import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()
TOKEN = os.getenv("TG-TOKEN")
BACK_URL = os.getenv("BACK-URL")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.text.startswith('/start '))
def handle_start_with_parameter(message: Message):
    parts = message.text.split(' ')
    
    if len(parts) < 2:
        bot.send_message(message.chat.id, "Неверный формат команды. Используйте: /start <uuid>")
        return

    payload = {
        "telegram_username": message.from_user.username or "unknown",
        "telegram_id": str(message.from_user.id),
        "application_uuid": parts[1],
    }

    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(
            url=f"{BACK_URL}/application/create", 
            json=payload, 
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            bot.send_message(message.chat.id, "Спасибо, вы отправили заявку")
        else:
            try:
                data = response.json()
                error_msg = data.get("detail", "Неизвестная ошибка")
            except:
                error_msg = f"HTTP ошибка: {response.status_code}"
            bot.send_message(message.chat.id, f'Произошла ошибка\n{error_msg}')
            
    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, f'Ошибка соединения с сервером: {str(e)}')

# Add error handler for the 409 conflict
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    pass  # Handle other messages if needed

if __name__ == '__main__':
    while True:
        try:
            print("Starting bot polling...")
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Error occurred: {e}")
            print("Restarting bot in 5 seconds...")
            time.sleep(5)