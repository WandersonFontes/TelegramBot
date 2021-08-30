from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Acount, Users, SendMessage, ReceivedMessage


class AcountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acount
        fields = [
            'bot_id', 
            'first_name', 
            'username', 
            'can_join_groups',
            'can_read_all_group_messages',
            'supports_inline_queries',
        ]


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = [
            'user_id', 
            'name', 
            'user', 
        ]


class SendMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SendMessage
        fields = [
            'user_id', 
            'text', 
        ]


class ReceivedMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReceivedMessage
        fields = [
            'user_id', 
            'text',
        ]
