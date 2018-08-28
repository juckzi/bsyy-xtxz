from django.contrib import admin
from django.urls import path,include
from .views import index

urlpatterns = [
    path('api/', include('servermanage.api.urls'),name='servermanage-api'),
    path('', index,name='index'),
]