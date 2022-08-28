from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly
from .models import Mailing, Client, Message
from .serializers import (
    MailingSerializer,
    ClientSerializer,
    MessageSerializer
)


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
    permission_classes = (IsAdminOrReadOnly, )

    @action(methods=["get"], detail=False)
    def complited_mailing(self, request):
        context = list()
        for mailing in Mailing.objects.all():
            context.append(
                {
                    "id": mailing.id,
                    "Всего сообщений": mailing.mailings.count(),
                    "Отправленых": mailing.mailings.filter(
                                        status_send="send"
                                    ).count(),
                    "Не отправленных": mailing.mailings.filter(
                                        status_send="no send"
                                    ).count(),
                }
            )
        return Response(context)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAdminOrReadOnly, )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAdminOrReadOnly, )
