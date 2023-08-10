from django.contrib import admin
from django import forms

from . import models


class TeknikBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeknikBooking
        fields = "__all__"


class TeknikBookingAdmin(admin.ModelAdmin):
    form = TeknikBookingAdminForm
    list_display = [
        "quantity",
        "created",
        "end",
        "start",
        "last_updated",
        "status",
    ]
    readonly_fields = [
        "quantity",
        "created",
        "end",
        "start",
        "last_updated",
        "status",
    ]


class TeknikItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeknikItem
        fields = "__all__"


class TeknikItemAdmin(admin.ModelAdmin):
    form = TeknikItemAdminForm
    list_display = [
        "name",
        "image",
        "last_updated",
        "created",
        "description",
    ]
    readonly_fields = [
        "name",
        "image",
        "last_updated",
        "created",
        "description",
    ]


class TeknikTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeknikType
        fields = "__all__"


class TeknikTypeAdmin(admin.ModelAdmin):
    form = TeknikTypeAdminForm
    list_display = [
        "name",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "name",
        "last_updated",
        "created",
    ]


admin.site.register(models.TeknikBooking, TeknikBookingAdmin)
admin.site.register(models.TeknikItem, TeknikItemAdmin)
admin.site.register(models.TeknikType, TeknikTypeAdmin)
