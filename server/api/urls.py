from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HostViewSet


router = DefaultRouter()
router.register('hosts',HostViewSet,base_name='api-host')
urlpatterns = router.urls
