from .serializers import AccountSerializer, UsersSerializer, SendMessageSerializer, ReceivedMessageSerializer     
from .models import Account, Users, SendMessage, ReceivedMessage
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from django.conf import settings


import requests, json


class AccountViewSet(viewsets.ModelViewSet):
    """
    Endpoint used to query the API and return BOT data.
    """
    token = settings.TELEGRAM_TOKEN
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    http_method_names = ['get']

    @action(detail=False, url_path='info', url_name='info', methods=['get'])
    def info(self, request):
        if not bool(self.queryset.count()):
            url = f'https://api.telegram.org/bot{self.token}/getMe'
            response = requests.get(url)
            data = response.json()
            serializer = self.serializer_class(data=data['result'])

            if serializer.is_valid():
                serializer.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UsersViewSet(viewsets.ModelViewSet):
    """
    Endpoint used to return user data and register in the database.
    """
    token = settings.TELEGRAM_TOKEN
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    http_method_names = ['get']

    @action(detail=False, url_path='updates', url_name='updates', methods=['get'])
    def updates(self, request):
        try:
            url = f'https://api.telegram.org/bot{self.token}/getUpdates'
            response = requests.get(url)
            data = response.json()
            for d in data['result']:
                if 'my_chat_member' in d:
                    user = Users.objects.filter(id=d['my_chat_member']['from']["id"])
                    key = 'my_chat_member'
                else:
                    user = Users.objects.filter(id=d['message']['from']["id"])
                    key = 'message'

                if user:
                    pass
                else:
                    userId = d[key]['from']['id']
                    d[key]['from']['name'] = d[key]['from']['first_name']+' '+d[key]['from']['last_name']
                    d[key]['from']['user'] = d[key]['from']['username'] if 'my_chat_member' in d[key]['from'] else d[key]['from']['first_name'].lower()
                    d[key]['from']['link'] = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={userId}&text=HELLO-WORD"
                    serializer = self.serializer_class(data=d[key]['from'])
                    if serializer.is_valid():
                        serializer.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            return HttpResponse('ERROR', status=201)
        

class SendMessageViewSet(viewsets.ModelViewSet):
    """
    Endpoint used to send messages and register them in the database.
    """
    token = settings.TELEGRAM_TOKEN
    queryset = SendMessage.objects.all()
    serializer_class = SendMessageSerializer
    http_method_names = ['get', 'post']

    @action(detail=False, url_path='send', url_name='send,', methods=['post'])
    def send(self, request):
        if request.data['user_id'].isdigit():
            user_id = request.data['user_id']
            url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={user_id}&text={request.data['text']}"
            response = requests.get(url)
            data = response.status_code
            if data == 200:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return HttpResponse('SEND MESSAGE SUCESSFULY', status=201)
            return HttpResponse('ERROR', status=404)
        else:
            user_id = request.data['user_id'].replace('http://127.0.0.1:8000/api/v1/users/', '')
            url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={user_id.replace('/','')}&text={request.data['text']}"
            response = requests.get(url)
            data = response.status_code
            if data == 200:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return HttpResponse('ERROR', status=404)


class ReceivedMessageViewSet(viewsets.ModelViewSet):
    """
    Endpoint to receive messages.
    """
    queryset = ReceivedMessage.objects.all()
    serializer_class = ReceivedMessageSerializer

    @action(detail=False, url_path='update', url_name='update', methods=['get'])
    def getUpdates(self, request):
        token = settings.TELEGRAM_TOKEN
        url = f'https://api.telegram.org/bot{token}/getMe'
        response = requests.get(url)
        data = response.json()
        return Response(data)
