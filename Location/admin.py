from django.contrib import admin
from django import forms

from . import models


class LocationTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.LocationType
        fields = "__all__"


class LocationTypeAdmin(admin.ModelAdmin):
    form = LocationTypeAdminForm
    list_display = [
        "created",
        "last_updated",
        "description",
        "name",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "description",
        "name",
    ]


class LocationBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.LocationBooking
        fields = "__all__"


class LocationBookingAdmin(admin.ModelAdmin):
    form = LocationBookingAdminForm
    list_display = [
        "end",
        "status",
        "remarks",
        "start",
        "created",
        "primary_camp",
        "last_updated",
    ]
    readonly_fields = [
        "end",
        "status",
        "remarks",
        "start",
        "created",
        "primary_camp",
        "last_updated",
    ]


class LocationItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.LocationItem
        fields = "__all__"


class LocationItemAdmin(admin.ModelAdmin):
    form = LocationItemAdminForm
    list_display = [
        "last_updated",
        "name",
        "created",
        "description",
    ]
    readonly_fields = [
        "last_updated",
        "name",
        "created",
        "description",
    ]


admin.site.register(models.LocationType, LocationTypeAdmin)
admin.site.register(models.LocationBooking, LocationBookingAdmin)
admin.site.register(models.LocationItem, LocationItemAdmin)
