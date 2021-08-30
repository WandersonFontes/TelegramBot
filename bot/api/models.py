from django.db import models
from django.conf import settings


class Acount(models.Model):
    token = settings.TELEGRAM_TOKEN
    bot_id = models.CharField(max_length=255, unique=True, primary_key=True)
    first_name = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    can_join_groups = models.BooleanField()
    can_read_all_group_messages = models.BooleanField()
    supports_inline_queries = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)


class Users(models.Model):
    user_id = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    user = models.CharField(max_length=255, unique=True)
    date_authorization = models.DateTimeField(auto_now_add=True)


class SendMessage(models.Model):
    user_id = models.ForeignKey(Acount, on_delete=models.CASCADE)
    text = models.TextField()
    date_shipping = models.DateTimeField(auto_now_add=True)


class ReceivedMessage(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    date_receivement = models.DateTimeField(auto_now_add=True)





