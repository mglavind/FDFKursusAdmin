from rest_framework import serializers

from . import models


class ButikkenItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ButikkenItem
        fields = [
            "description",
            "last_updated",
            "name",
            "created",
            "type",
        ]

class ButikkenBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ButikkenBooking
        fields = [
            "remarks",
            "quantity",
            "created",
            "status",
            "last_updated",
            "start",
            "team",
            "item",
            "team_contact",
        ]

class ButikkenItemTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ButikkenItemType
        fields = [
            "last_updated",
            "name",
            "created",
            "description",
        ]
