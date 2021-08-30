from django.conf import settings
from rest_framework import viewsets
from .serializers import AcountSerializer, UsersSerializer, SendMessageSerializer, ReceivedMessageSerializer     
from .models import Acount, Users, SendMessage, ReceivedMessage
import requests


class AcountViewSet(viewsets.ModelViewSet):
    """
    API endpoint to return account data(bot).
    """
    queryset = Acount.objects.all()
    serializer_class = AcountSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint to return authorized users.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class SendMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint to send messages.
    """
    queryset = SendMessage.objects.all()
    serializer_class = SendMessageSerializer


class ReceivedMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint to receive messages.
    """
    queryset = ReceivedMessage.objects.all()
    serializer_class = ReceivedMessageSerializer


#class Update():
def getUpdate(request):
    token = settings.TELEGRAM_TOKEN
    # url = 'https://api.telegram.org/bot'+token+'/getUpdates'
    url = 'https://api.telegram.org/bot1993429487:AAGddZhjZt_nnlfpW5GHj5yKRl8JZwEaE9o/getUpdates'
    response = requests.get(url)
    # transfor the response to json objects
    todos = response.json()
    return render(request, "main_app/home.html", {"response": todos})

