import os, requests, pytz
from dotenv import load_dotenv
from django.utils import timezone
from requests.exceptions import RequestException
from smtplib import SMTPException
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from celery import shared_task

from drf_mailing.celery import app
from .models import Mailing, Message, Client


log = get_task_logger(__name__)

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

@app.task(bind=True, retry_backoff=True, name='send_message')
def send_message(self, data, mailing_id, client_id, message_id):

    mailing = Mailing.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    client_timezone = client.time_zone
    now = timezone.localtime(timezone=pytz.timezone(client_timezone))

    if mailing.date_end > now:
        try:
            request = requests.post(
                f"{os.environ.get('URL_API')}{message_id}",
                headers = {
                    "Authorization": f"Bearer {os.environ.get('TOKEN')}",
                    "Content-Type": "application/json",
                    "accept": "application/json"
                },
                json = data,
            )
            if request.status_code // 100 < 3:
                Message.objects.update(status_send="send")
                log.info(f"Сообщение {message_id} отправлено")
            else:
                log.error(
                    f"Ответ с ошибкой {request.status_code} {request.reason}"
                )
                raise RequestException
        except RequestException as exc:
            log.error(f"Ошибка запроса {exc}")
            raise self.retry(exc=exc)
    else:
        total_time = (mailing.date_start - timezone.now())
        log.info(
            f"Сообщение будет отправлено через {total_time.total_seconds} секунд"
        )
        return self.retry(countdown=total_time.total_seconds())


@shared_task
def send_mail_task():
    mailings = Mailing.objects.all()
    message = str()

    for mailing in mailings:
        send = mailing.mailings.filter(status_send="send").count()
        no_send = mailing.mailings.filter(status_send="no send").count()
        message += f"""
            Рассылка №{mailing.id}
            Всего сообщений: {mailing.mailings.all().count()}
            Отправлено сообщений: {send}
            Не отправленно сообщений: {no_send}
            --------------------------------------
        """
    if message == "": message = "Рассылок не было"
    try:
        send_mail(
            'Статистика по обработанным рассылкам',
            message,
            os.environ.get("SERVER_EMAIL"),
            os.environ.get("SEND_STAT").split(","),
            fail_silently=False,
        )
        log.info('Письмо оправлено')
    except SMTPException as exc:
        log.error(f"Письмо не оправлено {exc}")
