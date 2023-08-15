from rest_framework import serializers

from . import models


class DepotItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DepotItem
        fields = [
            "created",
            "last_updated",
            "description",
            "name",
            "box",
        ]

class DepotLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DepotLocation
        fields = [
            "address",
            "name",
            "created",
            "last_updated",
            "description",
        ]

class DepotBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DepotBooking
        fields = [
            "remarks",
            "end",
            "last_updated",
            "created",
            "start",
            "status",
            "quantity",
            "team",
            "item",
            "team_contact",
        ]

class DepotBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DepotBox
        fields = [
            "name",
            "created",
            "last_updated",
            "description",
            "location",
        ]
