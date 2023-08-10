from django.contrib import admin
from django import forms

from . import models


class TeamAdminForm(forms.ModelForm):

    class Meta:
        model = models.Team
        fields = "__all__"


class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = [
        "name",
        "last_updated",
        "short_name",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class TeamMembershipAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeamMembership
        fields = "__all__"


class TeamMembershipAdmin(admin.ModelAdmin):
    form = TeamMembershipAdminForm
    list_display = [
        "member",
        "team",
        "role",
        "last_updated",
        "created",


    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = models.Event
        fields = "__all__"


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = [
        "name",
        "start_date",
        "end_date",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class EventMembershipAdminForm(forms.ModelForm):

    class Meta:
        model = models.EventMembership
        fields = "__all__"


class EventMembershipAdmin(admin.ModelAdmin):
    form = EventMembershipAdminForm
    list_display = [
        "member",
        "event",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class VolunteerAdminForm(forms.ModelForm):

    class Meta:
        model = models.Volunteer
        fields = "__all__"


class VolunteerAdmin(admin.ModelAdmin):
    form = VolunteerAdminForm
    list_display = [
        "email",
        "first_name",
        "last_name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.TeamMembership, TeamMembershipAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventMembership, EventMembershipAdmin)
admin.site.register(models.Volunteer, VolunteerAdmin)