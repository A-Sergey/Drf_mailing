from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from .models import Mailing, Client, Message
from .tasks import send_message


@receiver(post_save, sender=Mailing)
def create_mailing(sender, instance, created, **kwargs):
    if created:
        mailing = instance
        if mailing.filter == 'code':
            clients = Client.objects.filter(mobile_code=mailing.filter_name)
        else:
            clients = Client.objects.filter(tag=mailing.filter_name)

        for client in clients:
            message = Message.objects.create(
                mailing = mailing,
                client = client
            )
            date = {
                "id": message.id,
                "phone": client.phone_number,
                "text": mailing.message
            }

            if mailing.date_start <= timezone.now() <= mailing.date_end:
                send_message.apply_async(
                    (date, mailing.id, client.id, message.id),
                )
            elif mailing.date_start >= timezone.now() <= mailing.date_end:
                send_message.apply_async(
                    (date, mailing.id, client.id, message.id),
                    eta=mailing.date_start, 
                )
