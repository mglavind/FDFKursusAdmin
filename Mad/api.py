from rest_framework import viewsets, permissions

from . import serializers
from . import models


class MadItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the MadItem class"""

    queryset = models.MadItem.objects.all()
    serializer_class = serializers.MadItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class MadKategoriViewSet(viewsets.ModelViewSet):
    """ViewSet for the MadKategori class"""

    queryset = models.MadKategori.objects.all()
    serializer_class = serializers.MadKategoriSerializer
    permission_classes = [permissions.IsAuthenticated]


class MadBookingViewSet(viewsets.ModelViewSet):
    """ViewSet for the MadBooking class"""

    queryset = models.MadBooking.objects.all()
    serializer_class = serializers.MadBookingSerializer
    permission_classes = [permissions.IsAuthenticated]
