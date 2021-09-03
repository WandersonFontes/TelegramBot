from __future__ import absolute_import, unicode_literals
from .viewsets import UsersViewSet, SendMessageViewSet
from celery import shared_task
import time


@shared_task
def testTask():
    return 'Test of task!'

@shared_task
def checkNewUsers():
    UsersViewSet.updates(self, request)
    #return 'newUser'

@shared_task
def sendMessages():
    SendMessageViewSet.send(self, request)
    #return 'newUser'