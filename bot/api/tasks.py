from __future__ import absolute_import, unicode_literals
from .serializers import AccountSerializer, UsersSerializer, SendMessageSerializer, ReceivedMessageSerializer     
from .models import Account, Users, SendMessage, ReceivedMessage
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from django.conf import settings
import requests, json
from celery import shared_task

token = settings.TELEGRAM_TOKEN

@shared_task
def infoBot():
    '''
    Method to get bot data
    '''

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    if not bool(queryset.count()):
        url = f'https://api.telegram.org/bot{token}/getMe'
        response = requests.get(url)
        data = response.json()
        serializer = serializer_class(data=data['result'])
        
        if serializer.is_valid():
            serializer.save()
            return 'CREATED SUCESSFULY'
        return 'ERROR'
    return 'INFO ALREADY EXISTS'

@shared_task
def checkUpdates():
    '''
    Method to get data from authorized users
    '''

    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    url = f'https://api.telegram.org/bot{token}/getUpdates'
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
            d[key]['from']['link'] = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={userId}&text=HELLO-WORD"
            serializer = serializer_class(data=d[key]['from'])

            if serializer.is_valid():
                serializer.save()
                return 'UPDATED SUCESSFULY'
            return 'ERROR'
        return 'No news'

@shared_task
def sendMessage():
    '''
    Method to get send messages and save to database
    '''

    queryset = SendMessage.objects.all()
    serializer_class = SendMessageSerializer

    if request.data['user_id'].isdigit():
        user_id = request.data['user_id']
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={request.data['text']}"
        response = requests.get(url)
        data = response.status_code

        if data == 200:
            serializer = serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()
            return HttpResponse('SEND MESSAGE SUCESSFULY', status=201)
        return HttpResponse('ERROR', status=404)

    else:
        user_id = request.data['user_id'].replace('http://127.0.0.1:8000/api/v1/users/', '')
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id.replace('/','')}&text={request.data['text']}"
        response = requests.get(url)
        data = response.status_code

        if data == 200:
            serializer = serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        #return HttpResponse('ERROR', status=404)
