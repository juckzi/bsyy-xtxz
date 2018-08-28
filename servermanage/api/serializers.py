from rest_framework import serializers
from servermanage.models import Host


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'
