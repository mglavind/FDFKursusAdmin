from django.contrib import admin
from django import forms

from . import models


class MadItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.MadItem
        fields = "__all__"


class MadItemAdmin(admin.ModelAdmin):
    form = MadItemAdminForm
    list_display = [
        "last_updated",
        "indhold",
        "er_aktiv",
        "enhed",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "indhold",
        "er_aktiv",
        "enhed",
        "created",
    ]


class MadKategoriAdminForm(forms.ModelForm):

    class Meta:
        model = models.MadKategori
        fields = "__all__"


class MadKategoriAdmin(admin.ModelAdmin):
    form = MadKategoriAdminForm
    list_display = [
        "created",
        "navn",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "navn",
        "last_updated",
    ]


class MadBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.MadBooking
        fields = "__all__"


class MadBookingAdmin(admin.ModelAdmin):
    form = MadBookingAdminForm
    list_display = [
        "aktivitet",
        "forklaring",
        "antal",
        "last_updated",
        "status",
        "created",
        "anvendelses_tidspunkt",
    ]
    readonly_fields = [
        "aktivitet",
        "forklaring",
        "antal",
        "last_updated",
        "status",
        "created",
        "anvendelses_tidspunkt",
    ]


admin.site.register(models.MadItem, MadItemAdmin)
admin.site.register(models.MadKategori, MadKategoriAdmin)
admin.site.register(models.MadBooking, MadBookingAdmin)
