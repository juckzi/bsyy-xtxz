from server.models import Host
from .serializers import HostSerializer
from rest_framework import viewsets, filters


class HostViewSet(viewsets.ModelViewSet):
    serializer_class = HostSerializer
    queryset = Host.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = '__all__'

