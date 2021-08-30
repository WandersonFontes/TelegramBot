from django.contrib import admin
from .models import Acount, Users, SendMessage, ReceivedMessage


@admin.register(Acount)
class AcountAdmin(admin.ModelAdmin):
    model = Acount


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    model = Users


@admin.register(SendMessage)
class SendMessageAdmin(admin.ModelAdmin):
    model = SendMessage

    
@admin.register(ReceivedMessage)
class ReceivedMessageAdmin(admin.ModelAdmin):
    model = ReceivedMessage
