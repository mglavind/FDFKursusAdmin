from django.contrib import admin
from django import forms

from . import models


class ButikkenItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenItem
        fields = "__all__"


class ButikkenItemAdmin(admin.ModelAdmin):
    form = ButikkenItemAdminForm
    list_display = [
        "description",
        "last_updated",
        "name",
        "created",
    ]
    readonly_fields = [
        "description",
        "last_updated",
        "name",
        "created",
    ]


class ButikkenBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenBooking
        fields = "__all__"


class ButikkenBookingAdmin(admin.ModelAdmin):
    form = ButikkenBookingAdminForm
    list_display = [
        "remarks",
        "quantity",
        "created",
        "status",
        "last_updated",
        "start",
    ]
    readonly_fields = [
        "remarks",
        "quantity",
        "created",
        "status",
        "last_updated",
        "start",
    ]


class ButikkenItemTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenItemType
        fields = "__all__"


class ButikkenItemTypeAdmin(admin.ModelAdmin):
    form = ButikkenItemTypeAdminForm
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


admin.site.register(models.ButikkenItem, ButikkenItemAdmin)
admin.site.register(models.ButikkenBooking, ButikkenBookingAdmin)
admin.site.register(models.ButikkenItemType, ButikkenItemTypeAdmin)
