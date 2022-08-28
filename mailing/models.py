from django.db import models
from django.core.validators import RegexValidator
from pytz import all_timezones


class Mailing(models.Model):
    choice_filter = (
        ("code", "Code"),
        ("tag", "Tag"),
    )

    date_start = models.DateTimeField()
    filter = models.CharField(max_length=15, choices=choice_filter)
    filter_name = models.CharField(max_length=50)
    date_end = models.DateTimeField()
    message = models.TextField(max_length=200)
    send_period_time_start = models.TimeField()
    send_period_time_end = models.TimeField()

    def __str__(self):
        return f"Рассылка №{self.id}"


class Client(models.Model):
    choice_time_zones = tuple(zip(all_timezones, all_timezones))

    phone_number_validators = RegexValidator(
        regex=r"^7\d{10}$",
        message="Номер телефона в формате 7XXXXXXXXXX (X - цифра от 0 до 9)"
    )

    phone_number = models.CharField(
        max_length=11, validators=[phone_number_validators], unique=True
    )
    mobile_code = models.CharField(max_length=3, blank=True)
    tag = models.CharField(max_length=15, blank=True)
    time_zone = models.CharField(
        max_length=32, choices=choice_time_zones, default="UTC"
    )

    def save(self, *args, **kwargs):
        self.mobile_code = str(self.phone_number)[1:4]
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Клиент +7({self.mobile_code})-{self.phone_number[4:]}"


class Message(models.Model):
    choice_status_send = (
        ("send", "Send"),
        ("no send", "No send"),
    )

    create = models.DateTimeField(auto_now_add=True)
    status_send = models.CharField(
        max_length=10, choices=choice_status_send, default="no send"
    )
    mailing = models.ForeignKey(
        Mailing, related_name="mailings", on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        Client, related_name="clients", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.mailing} {self.client}".replace('т','ту')
