from rest_framework import viewsets
from .models import CpuUsage
from .serializers import CpuUsageSerializer


class CpuUsageViewSet(viewsets.ModelViewSet):
    queryset = CpuUsage.objects.all().order_by('-timestamp')[:100]
    serializer_class = CpuUsageSerializer
