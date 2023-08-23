from django.contrib import admin
from django import forms

from . import models


class DepotItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotItem
        fields = "__all__"


class DepotItemAdmin(admin.ModelAdmin):
    form = DepotItemAdminForm
    list_display = [
        "name",
        "description",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "last_updated",
        "description",
    ]


class DepotLocationAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotLocation
        fields = "__all__"


class DepotLocationAdmin(admin.ModelAdmin):
    form = DepotLocationAdminForm
    list_display = [
        "name",
        "description",
        "address",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class DepotBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotBooking
        fields = "__all__"


class DepotBookingAdmin(admin.ModelAdmin):
    form = DepotBookingAdminForm
    list_display = [
        "item",
        "quantity",
        "team",
        "team_contact",
        "remarks",
        "start",
        "end",
        "status",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class DepotBoxAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotBox
        fields = "__all__"


class DepotBoxAdmin(admin.ModelAdmin):
    form = DepotBoxAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
        "description",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.DepotItem, DepotItemAdmin)
admin.site.register(models.DepotLocation, DepotLocationAdmin)
admin.site.register(models.DepotBooking, DepotBookingAdmin)
admin.site.register(models.DepotBox, DepotBoxAdmin)
