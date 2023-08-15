from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ButikkenItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the ButikkenItem class"""

    queryset = models.ButikkenItem.objects.all()
    serializer_class = serializers.ButikkenItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class ButikkenBookingViewSet(viewsets.ModelViewSet):
    """ViewSet for the ButikkenBooking class"""

    queryset = models.ButikkenBooking.objects.all()
    serializer_class = serializers.ButikkenBookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ButikkenItemTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the ButikkenItemType class"""

    queryset = models.ButikkenItemType.objects.all()
    serializer_class = serializers.ButikkenItemTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
