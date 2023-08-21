from django.contrib import admin
from django import forms

from . import models


class AktivitetsTeamItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.AktivitetsTeamItem
        fields = "__all__"


class AktivitetsTeamItemAdmin(admin.ModelAdmin):
    form = AktivitetsTeamItemAdminForm
    list_display = [
        "description",
        "created",
        "last_updated",
        "name",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class AktivitetsTeamBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.AktivitetsTeamBooking
        fields = "__all__"


class AktivitetsTeamBookingAdmin(admin.ModelAdmin):
    form = AktivitetsTeamBookingAdminForm
    list_display = [
        "created",
        "last_updated",
        "location",
        "start_date",
        "end_date",
        "remarks",
        "status",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.AktivitetsTeamItem, AktivitetsTeamItemAdmin)
admin.site.register(models.AktivitetsTeamBooking, AktivitetsTeamBookingAdmin)
