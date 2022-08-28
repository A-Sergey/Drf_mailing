import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_mailing.settings")

app = Celery("drf_mailing")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
