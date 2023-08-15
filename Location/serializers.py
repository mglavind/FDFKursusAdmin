from rest_framework import serializers

from . import models


class LocationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LocationType
        fields = [
            "created",
            "last_updated",
            "description",
            "name",
        ]

class LocationBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LocationBooking
        fields = [
            "end",
            "status",
            "remarks",
            "start",
            "created",
            "primary_camp",
            "last_updated",
            "team_contact",
            "item",
            "team",
        ]

class LocationItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LocationItem
        fields = [
            "last_updated",
            "name",
            "created",
            "description",
            "type",
        ]
