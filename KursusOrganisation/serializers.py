from rest_framework import serializers

from . import models


class MedarbejderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Medarbejder
        fields = [
            "date_created",
            "last_updated",
            "navn",
            "user",
        ]

class KursusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Kursus
        fields = [
            "start_date",
            "last_updated",
            "date_created",
            "navn",
            "end_date",
        ]

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Team
        fields = [
            "last_updated",
            "navn",
            "date_created",
            "medarbejder",
            "kursus",
        ]
