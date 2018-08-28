from xxxt.models import download,sysdownload
from .serializers import downloadSerializer,sysdownloadSerializer
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend

class downloadViewSet(viewsets.ModelViewSet):
    serializer_class = downloadSerializer
    queryset = download.objects.all()
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter,)
    search_fields = ('id','name','vendor','phone','comment')
    filter_fields = ('id','name')
    ordering_fields = ('name')
     

class sysdownloadViewSet(viewsets.ModelViewSet):
    serializer_class = sysdownloadSerializer
    queryset = sysdownload.objects.all()
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter,)
    search_fields = ('id','name','download__name')
    filter_fields = ('id','name')
    ordering_fields = ('name')
