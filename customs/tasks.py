from celery import shared_task
from customs.models import Customs

import datetime
from customs.services import send_telegram_message


@shared_task
def send_custom():
    customs = Customs.objects.all()
    current_date = datetime.datetime.now()  # Текущее время
    for custom in customs:
        if custom.time >= current_date:
            tg_chat = custom.user.tg_chat_id
            message = f"Я буду {custom.action} в {custom.time} в {custom.place}."
            send_telegram_message(tg_chat, message)  # Отправляем привычку в Telegram чат