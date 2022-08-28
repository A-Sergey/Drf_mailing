from django.contrib import admin

from .models import Mailing, Client, Message


class MailingtAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "filter",
        "filter_name",
        "date_start",
        "date_end",
    )
    search_fields = (
        "message",
        "filter",
        "filter_name",
        "date_start",
        "date_end",
    )


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "mobile_code",
        "tag",
        "time_zone",
    )
    search_fields = (
        "phone_number",
        "mobile_code",
        "tag",
        "time_zone",
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "mailing",
        "create",
        "status_send",
    )
    search_fields = (
        "client",
        "mailing",
        "create",
        "status_send",
    )


admin.site.register(Mailing, MailingtAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)
