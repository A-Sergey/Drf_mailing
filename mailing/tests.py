from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Mailing, Client, Message


class TestModels(TestCase):
    def test_create_mailing(self):
        mailing = Mailing.objects.create(
            date_start = timezone.now(), message = "Test text",
            filter="CODE", filter_name="111",
            date_end=timezone.now() + datetime.timedelta(days=1),
            send_period_time_start=timezone.now(),
            send_period_time_end = (
                timezone.now() + datetime.timedelta(days=1)
            ).time()
        )
        
        self.assertIsInstance(mailing, Mailing)
        self.assertIsInstance(mailing.message, str)
        self.assertEqual(mailing.filter, "CODE")
        self.assertEqual(mailing.filter_name, "111")

    def test_create_client(self):
        client = Client.objects.create(
            phone_number="71231231235", tag="tag",
            time_zone="Europe/Moscow"
        )
        
        self.assertIsInstance(client, Client)
        self.assertIsInstance(client.phone_number, str)
        self.assertEqual(client.phone_number, "71231231235")
        self.assertEqual(client.tag, "tag")
        self.assertEqual(client.time_zone, "Europe/Moscow")

    def test_create_message(self):
        mailing = Mailing.objects.create(
            date_start = timezone.now(), message = "Test text",
            filter="CODE", filter_name="111",
            date_end=timezone.now() + datetime.timedelta(days=1),
            send_period_time_start=timezone.now(),
            send_period_time_end = (
                timezone.now() + datetime.timedelta(days=1)
            ).time()
        )
        
        client = Client.objects.create(
            phone_number="71231231235", tag="tag",
            time_zone="Europe/Moscow"
        )
        
        message = Message.objects.create(
            create=timezone.now(), status_send="SEND",
            mailing_id=mailing.id, client_id=client.id
        )
        
        self.assertIsInstance(message, Message)
        self.assertEqual(message.status_send, "SEND")
