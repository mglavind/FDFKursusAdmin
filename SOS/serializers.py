from rest_framework import serializers

from . import models


class SOSBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SOSBooking
        fields = [
            "quantity",
            "created",
            "end",
            "start",
            "last_updated",
            "status",
            "team",
            "item",
            "team_contact",
        ]

class SOSItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SOSItem
        fields = [
            "name",
            "last_updated",
            "created",
            "description",
        ]

class SOSTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SOSType
        fields = [
            "name",
            "last_updated",
            "created",
        ]
