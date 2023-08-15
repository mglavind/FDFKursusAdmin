from rest_framework import viewsets, permissions

from . import serializers
from . import models


class DepotItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the DepotItem class"""

    queryset = models.DepotItem.objects.all()
    serializer_class = serializers.DepotItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepotLocationViewSet(viewsets.ModelViewSet):
    """ViewSet for the DepotLocation class"""

    queryset = models.DepotLocation.objects.all()
    serializer_class = serializers.DepotLocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepotBookingViewSet(viewsets.ModelViewSet):
    """ViewSet for the DepotBooking class"""

    queryset = models.DepotBooking.objects.all()
    serializer_class = serializers.DepotBookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepotBoxViewSet(viewsets.ModelViewSet):
    """ViewSet for the DepotBox class"""

    queryset = models.DepotBox.objects.all()
    serializer_class = serializers.DepotBoxSerializer
    permission_classes = [permissions.IsAuthenticated]
