from rest_framework import serializers

from . import models


class MadItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MadItem
        fields = [
            "last_updated",
            "indhold",
            "er_aktiv",
            "enhed",
            "created",
            "kategori",
        ]

class MadKategoriSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MadKategori
        fields = [
            "created",
            "navn",
            "last_updated",
        ]

class MadBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MadBooking
        fields = [
            "aktivitet",
            "forklaring",
            "antal",
            "last_updated",
            "status",
            "created",
            "anvendelses_tidspunkt",
        ]
