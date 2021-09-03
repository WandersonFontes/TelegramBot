from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import AccountViewSet, UsersViewSet, SendMessageViewSet, ReceivedMessageViewSet
# from .api.views import getUpdate

route = routers.DefaultRouter()
route.register(r'account', AccountViewSet)
route.register(r'users', UsersViewSet)
route.register(r'messages', SendMessageViewSet)
route.register(r'received', ReceivedMessageViewSet)
#route.register(r'update', getUpdates, basename='getUpdate')
# route.register(r'up', getUpdate, basename='getUpdate')


urlpatterns = [
    #path('updates/', getUpdates, name='getUpdates'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(route.urls)),
    #path('api-auth/', include('rest_framework.urls'))
]

#path('questions/', apiviews.questions_view, name='questions_view'),