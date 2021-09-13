from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from django.conf import settings
from .tasks import *
from .serializers import *
from .models import *
import requests
import time


class AccountViewSet(viewsets.ModelViewSet):
    """
    Endpoint used to query the API and return BOT data.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    http_method_names = ['get']

    @action(detail=False, url_path='info', url_name='info', methods=['get'])
    def infoBot(self, request):
        try:
            infoBot.delay()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception():
            return HttpResponse('ERROR', status=404)
        

class UsersViewSet(viewsets.ModelViewSet):
    """
    Endpoint used to return user data and register in the database.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    http_method_names = ['get']

    @action(detail=False, url_path='updates', url_name='updates', methods=['get'])
    def checkUpdates(self, request):
        try:
            checkUpdates.delay()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            return HttpResponse('ERROR', status=404)

    @action(detail=False, url_path='autoup', url_name='autoup', methods=['get'])
    def autoUpdates(self, request):
        try:
            while 1 == 1:
                time.sleep(5)
                checkUpdates.delay()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            return HttpResponse('ERROR', status=404)
        

class SendMessageViewSet(viewsets.ModelViewSet):
    """
    Endpoint used to send messages and register them in the database.
    """
    queryset = SendMessage.objects.all()
    serializer_class = SendMessageSerializer
    http_method_names = ['get', 'post']
    token = settings.TELEGRAM_TOKEN


    @action(detail=False, url_path='send', url_name='send', methods=['post'])
    def sendMessage(self, request):
        try:
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
        except Exception as e:
            return HttpResponse('ERROR', status=404)
    


class ReceivedMessageViewSet(viewsets.ModelViewSet):
    """
    Endpoint to receive messages.
    """
    queryset = ReceivedMessage.objects.all()
    serializer_class = ReceivedMessageSerializer





