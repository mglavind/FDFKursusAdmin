from rest_framework import viewsets, permissions

from . import serializers
from . import models


class MedarbejderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Medarbejder class"""

    queryset = models.Medarbejder.objects.all()
    serializer_class = serializers.MedarbejderSerializer
    permission_classes = [permissions.IsAuthenticated]


class KursusViewSet(viewsets.ModelViewSet):
    """ViewSet for the Kursus class"""

    queryset = models.Kursus.objects.all()
    serializer_class = serializers.KursusSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for the Team class"""

    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
