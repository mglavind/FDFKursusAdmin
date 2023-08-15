from django.contrib import admin
from django import forms

from . import models


class FotoItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.FotoItem
        fields = "__all__"


class FotoItemAdmin(admin.ModelAdmin):
    form = FotoItemAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class FotoBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.FotoBooking
        fields = "__all__"


class FotoBookingAdmin(admin.ModelAdmin):
    form = FotoBookingAdminForm
    list_display = [
        "start",
        "end",
        "remarks",
        "created",
        "location",
        "last_updated",
        "status",
    ]
    readonly_fields = [
        "start",
        "end",
        "remarks",
        "created",
        "location",
        "last_updated",
        "status",
    ]


admin.site.register(models.FotoItem, FotoItemAdmin)
admin.site.register(models.FotoBooking, FotoBookingAdmin)
