from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import *
route = routers.DefaultRouter()
route.register(r'account', AccountViewSet)
route.register(r'users', UsersViewSet)
route.register(r'messages', SendMessageViewSet)
route.register(r'received', ReceivedMessageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(route.urls)),
]
