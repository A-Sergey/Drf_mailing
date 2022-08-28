from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mailing.views import MailingViewSet, ClientViewSet, MessageViewSet
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r"mailings", MailingViewSet)
router.register(r"clients", ClientViewSet)
router.register(r"messages", MessageViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/api-auth/", include("rest_framework.urls")),
    path("api/v1/", include(router.urls)),
]

urlpatterns += doc_urls
