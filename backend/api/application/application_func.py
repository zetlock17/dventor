import requests
from ..exceptions import BotSendMessageErrorHttpException
from config import TG_TOKEN

TOKEN = TG_TOKEN
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


async def bot_send_message(text: str, chat_id: int):

    payload = {
        'chat_id': chat_id,
        'text': text
    }

    try:
        response = requests.post(URL, data=payload)

        if response.status_code != 200:
            raise BotSendMessageErrorHttpException()

    except requests.exceptions.RequestException as e:
        raise e