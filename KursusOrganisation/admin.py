from django.contrib import admin
from django import forms

from . import models


class MedarbejderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Medarbejder
        fields = "__all__"


class MedarbejderAdmin(admin.ModelAdmin):
    form = MedarbejderAdminForm
    list_display = [
        "date_created",
        "last_updated",
        "navn",
        "telefon_nummer",
        "medarbejder_email",
    ]
    readonly_fields = [
        "date_created",
    ]


class KursusAdminForm(forms.ModelForm):

    class Meta:
        model = models.Kursus
        fields = "__all__"


class KursusAdmin(admin.ModelAdmin):
    form = KursusAdminForm
    list_display = [
        "start_date",
        "last_updated",
        "date_created",
        "navn",
        "end_date",
    ]
    readonly_fields = [
        "start_date",
        "date_created",
        "navn",
        "end_date",
    ]


class TeamAdminForm(forms.ModelForm):

    class Meta:
        model = models.Team
        fields = "__all__"


class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = [
        "last_updated",
        "navn",
        "date_created",
    ]
    readonly_fields = [
        "last_updated",
        "navn",
        "date_created",
    ]


admin.site.register(models.Medarbejder, MedarbejderAdmin)
admin.site.register(models.Kursus, KursusAdmin)
admin.site.register(models.Team, TeamAdmin)
