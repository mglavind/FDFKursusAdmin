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


class DepotLocationAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotLocation
        fields = "__all__"


class DepotLocationAdmin(admin.ModelAdmin):
    form = DepotLocationAdminForm
    list_display = [
        "address",
        "name",
        "created",
        "last_updated",
        "description",
    ]
    readonly_fields = [
        "address",
        "name",
        "created",
        "last_updated",
        "description",
    ]


class DepotBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotBooking
        fields = "__all__"


class DepotBookingAdmin(admin.ModelAdmin):
    form = DepotBookingAdminForm
    list_display = [
        "remarks",
        "end",
        "last_updated",
        "created",
        "start",
        "status",
        "quantity",
    ]
    readonly_fields = [
        "remarks",
        "end",
        "last_updated",
        "created",
        "start",
        "status",
        "quantity",
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
        "name",
        "created",
        "last_updated",
        "description",
    ]


admin.site.register(models.DepotItem, DepotItemAdmin)
admin.site.register(models.DepotLocation, DepotLocationAdmin)
admin.site.register(models.DepotBooking, DepotBookingAdmin)
admin.site.register(models.DepotBox, DepotBoxAdmin)
