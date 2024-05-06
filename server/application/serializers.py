from rest_framework import serializers
from .models import CpuUsage


class CpuUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuUsage
        fields = ['id', 'timestamp', 'usage']
