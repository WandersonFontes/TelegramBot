from django.contrib import admin
from .models import Account, Users, SendMessage, ReceivedMessage


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    model = Users


@admin.register(SendMessage)
class SendMessageAdmin(admin.ModelAdmin):
    model = SendMessage

    
@admin.register(ReceivedMessage)
class ReceivedMessageAdmin(admin.ModelAdmin):
    model = ReceivedMessage
