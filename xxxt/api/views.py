from xxxt.models import download, sysdownload
from .serializers import downloadSerializer, sysdownloadSerializer
from rest_framework import viewsets, filters


class downloadViewSet(viewsets.ModelViewSet):
    serializer_class = downloadSerializer
    queryset = download.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name', 'vendor', 'phone', 'comment')


class sysdownloadViewSet(viewsets.ModelViewSet):
    serializer_class = sysdownloadSerializer
    queryset = sysdownload.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name', 'download__name')
