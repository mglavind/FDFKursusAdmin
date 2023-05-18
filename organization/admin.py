from django.contrib import admin
from .models import Volunteer, Team, TeamMembership, Event, EventMembership


admin.site.register(Volunteer)
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(EventMembership)
class EventMembershipAdmin(admin.ModelAdmin):
    pass

