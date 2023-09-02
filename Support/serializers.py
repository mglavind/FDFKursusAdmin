from rest_framework import serializers

from . import models


class SupportItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SupportItem
        fields = [
            "name",
            "description",
            "created",
            "last_updated",
            "type",
        ]

class SupportBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SupportBooking
        fields = [
            "remarks",
            "last_updated",
            "created",
            "status",
            "start",
            "end",
            "item",
            "team_contact",
            "team",
        ]

class SupportItemTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SupportItemType
        fields = [
            "name",
            "description",
            "created",
            "last_updated",
        ]
