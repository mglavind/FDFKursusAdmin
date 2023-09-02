from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SupportItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the SupportItem class"""

    queryset = models.SupportItem.objects.all()
    serializer_class = serializers.SupportItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupportBookingViewSet(viewsets.ModelViewSet):
    """ViewSet for the SupportBooking class"""

    queryset = models.SupportBooking.objects.all()
    serializer_class = serializers.SupportBookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupportItemTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the SupportItemType class"""

    queryset = models.SupportItemType.objects.all()
    serializer_class = serializers.SupportItemTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
