from django.db import models
from django.conf import settings


class Account(models.Model):
    token = settings.TELEGRAM_TOKEN
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    first_name = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    can_join_groups = models.BooleanField()
    can_read_all_group_messages = models.BooleanField()
    supports_inline_queries = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username


class Users(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255, unique=True)
    link = models.URLField(max_length=200, unique=True)
    date_authorization = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_authorization',)
    def __str__(self):
        return self.name


class SendMessage(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    date_shipping = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("date_shipping",)
    def __str__(self):
        return self.user_id


class ReceivedMessage(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    date_receivement = models.DateTimeField(auto_now_add=True)





