from rest_framework import viewsets, permissions

from . import serializers
from . import models


class LocationTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the LocationType class"""

    queryset = models.LocationType.objects.all()
    serializer_class = serializers.LocationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationBookingViewSet(viewsets.ModelViewSet):
    """ViewSet for the LocationBooking class"""

    queryset = models.LocationBooking.objects.all()
    serializer_class = serializers.LocationBookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the LocationItem class"""

    queryset = models.LocationItem.objects.all()
    serializer_class = serializers.LocationItemSerializer
    permission_classes = [permissions.IsAuthenticated]
