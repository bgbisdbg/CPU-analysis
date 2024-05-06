from django.db import models


class CpuUsage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    usage = models.FloatField()