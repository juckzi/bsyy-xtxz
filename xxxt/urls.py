from django.contrib import admin
from django.urls import path,include
from .views import index


app_name = 'xxxt'
urlpatterns = [
    path('api/', include('xxxt.api.urls'),name='api'),
    path('', index,name='index'),
]