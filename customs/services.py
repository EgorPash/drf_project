import requests
from my_project.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, message):
    """
    Отправка сообщения в телеграм чат
    :param chat_id: id чата
    :param message: текст сообщения
    return:
    """
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)