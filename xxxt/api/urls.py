from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import downloadViewSet,sysdownloadViewSet


router = DefaultRouter()
router.register('downloads',downloadViewSet,base_name='api-download')
router.register('sysdownloads',sysdownloadViewSet,base_name='api-sysdownload')
urlpatterns = router.urls
