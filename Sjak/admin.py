from django.contrib import admin
from django import forms

from . import models


class SjakItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.SjakItem
        fields = "__all__"


class SjakItemAdmin(admin.ModelAdmin):
    form = SjakItemAdminForm
    list_display = [
        "name",
        "description",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "name",
        "description",
        "created",
        "last_updated",
    ]


class SjakBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.SjakBooking
        fields = "__all__"


class SjakBookingAdmin(admin.ModelAdmin):
    form = SjakBookingAdminForm
    list_display = [
        "remarks",
        "last_updated",
        "created",
        "status",
        "quantity",
        "use_date",
    ]
    readonly_fields = [
        "remarks",
        "last_updated",
        "created",
        "status",
        "quantity",
        "use_date",
    ]


class SjakItemTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.SjakItemType
        fields = "__all__"


class SjakItemTypeAdmin(admin.ModelAdmin):
    form = SjakItemTypeAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "name",
        "created",
        "last_updated",
    ]


admin.site.register(models.SjakItem, SjakItemAdmin)
admin.site.register(models.SjakBooking, SjakBookingAdmin)
admin.site.register(models.SjakItemType, SjakItemTypeAdmin)
