import telebot
from telebot.types import Message
import os
from dotenv import load_dotenv
import requests


load_dotenv()
TOKEN = os.getenv("TG-TOKEN")
BACK_URL = os.getenv("BACK-URL")

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.reply_to(message, "Привет я бот для сервиса наставников")

@bot.message_handler(func=lambda message: message.text.startswith('/start '))
def handle_start_with_parameter(message: Message):

    parts = message.text.split(' ')

    payload = {
        "application_uuid": parts[1],
        "telegram_username": message.from_user.username,
        "telegram_id": message.from_user.id
    }

    response = requests.post(url=BACK_URL, data=payload)

    if response.status_code == 200:
        bot.send_message(chat_id=message.chat.id, text="Спасибо, вы отправили заявку")
    else:
        bot.send_message(chat_id=message.chat.id, text=f'Произошла ошибка {response.status_code}')
    

bot.polling()