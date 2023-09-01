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
        "name",
        "description",
        "created",
        "last_updated",
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
        "item",
        "team",
        "team_contact",
        "status",
        "start_date",
        "end_date",
        "remarks",
        "location",
        "remarks_internal",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.AktivitetsTeamItem, AktivitetsTeamItemAdmin)
admin.site.register(models.AktivitetsTeamBooking, AktivitetsTeamBookingAdmin)
