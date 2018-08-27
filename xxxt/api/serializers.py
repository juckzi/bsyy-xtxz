from rest_framework import serializers
from xxxt.models import download,sysdownload


class downloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = download
        fields = (
            'id',
            'name',
            'vendor',
            'phone',
            'comment',
        )


class sysdownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = sysdownload
        fields = (
            'id',
            'download',
            'name',
            'url',
        )