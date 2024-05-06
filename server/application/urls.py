from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CpuUsageViewSet

router = DefaultRouter()
router.register(r'application', CpuUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]