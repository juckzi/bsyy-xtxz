from django.contrib import admin
from django.urls import path,include
from .views import index

urlpatterns = [
    path('api/', include('server.api.urls'),name='server-api'),
    path('', index,name='index'),
]