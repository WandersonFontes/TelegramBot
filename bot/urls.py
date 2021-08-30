from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.views import AcountViewSet, UsersViewSet, SendMessageViewSet, ReceivedMessageViewSet
# from .api.views import getUpdate

route = routers.DefaultRouter()
route.register(r'account', AcountViewSet)
route.register(r'users', UsersViewSet)
route.register(r'send', SendMessageViewSet)
route.register(r'received', ReceivedMessageViewSet)
# route.register(r'up', getUpdate, basename='getUpdate')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(route.urls)),
    #path('api-auth/', include('rest_framework.urls'))
]
