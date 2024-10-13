from typing import List
from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.urls import path
from django.shortcuts import render
from Butikken.models import MealPlan, TeamMealPlan
from organization.models import Team, TeamMembership, TeamEventMembership, EventMembership, Event
from django.db.models import Min
from datetime import date
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.urls.resolvers import URLPattern
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from .models import Volunteer
import random
from datetime import datetime
import csv

from . import models


class TeamAdminForm(forms.ModelForm):

    class Meta:
        model = models.Team
        fields = "__all__"



class TeamEventMembershipInline(admin.TabularInline):
    model = TeamEventMembership
    extra = 1

def create_team_meal_plans(modeladmin, request, queryset):
    meal_plans = MealPlan.objects.all()
    created_count = 0
    for team in queryset:
        for meal_plan in meal_plans:
            # Check if the TeamMealPlan already exists
            if not TeamMealPlan.objects.filter(team=team, meal_plan=meal_plan).exists():
                TeamMealPlan.objects.create(team=team, meal_plan=meal_plan)
                created_count += 1
    modeladmin.message_user(request, f"{created_count} TeamMealPlan objects created successfully.")

create_team_meal_plans.short_description = "Create TeamMealPlan for each MealPlan"


class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    #inlines = [TeamEventMembershipInline]
    list_display = [
        "id",
        "name",
        "short_name",
    #    "display_events",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    actions = [create_team_meal_plans]
    #def display_events(self, obj):
    #    return ", ".join([event.name for event in obj.events.all()])


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
        "id",
        "name",
        "start_date",
        "end_date",  
        "is_active",  
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "id",
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
        "volunteer",
        "event",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class TeamEventMembershipAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeamEventMembership
        fields = "__all__"


class TeamEventMembershipAdmin(admin.ModelAdmin):
    form = TeamEventMembershipAdminForm
    list_display = [
        "team",
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

    

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class EventMembershipInline(admin.TabularInline):
    model = EventMembership
    extra = 1

class TeamMembershipInline(admin.TabularInline):
    model = TeamMembership
    extra = 1




class VolunteerAdmin(admin.ModelAdmin):
    form = VolunteerAdminForm
    inlines = [EventMembershipInline, TeamMembershipInline]
    list_display = [
        "first_name",
        "last_name",
        "username",
        "email",
        "phone",
        "display_events",
        "display_teams",
        "created",
        "last_updated",
        "is_active",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    actions = ["export_to_csv", "send_email_action", "deactivate_volunteers", "activate_volunteers", "create_event_membership", "assign_to_aktivitetsteam_group"]
    search_fields = ['first_name', 'last_name', 'email', 'username'] 
    list_filter = (
        ('is_active', ChoiceDropdownFilter),
        ('last_updated', DropdownFilter),
        ('events', RelatedDropdownFilter),
        ('teams', RelatedDropdownFilter),
    )

    def display_events(self, obj):
        return ", ".join([event.name for event in obj.events.all()])
    def display_teams(self, obj):
        return ", ".join([team.name for team in obj.teams.all()])
    
    def export_to_csv(modeladmin, request, queryset):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="volunteers.csv"'
            response.write(u'\ufeff'.encode('utf8'))

            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Username', 'Email', 'Phone', 'events'])

            for volunteer in queryset:
                writer.writerow([volunteer.first_name, volunteer.last_name, volunteer.username, volunteer.email, volunteer.phone,  volunteer.events])
            return response
    export_to_csv.short_description = "Export selected volunteers to CSV"
    
    def get_urls(self) -> List[URLPattern]:
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def assign_to_aktivitetsteam_group(self, request, queryset):
        group, created = Group.objects.get_or_create(name="AktivitetstTeamBookingTildeling")
        for volunteer in queryset:
            volunteer.groups.add(group)
        self.message_user(request, f"Selected volunteers have been assigned to the group 'AktivitetstTeamBookingTildeling'.")
    assign_to_aktivitetsteam_group.short_description = "Assign selected volunteers to AktivitetstTeamBookingTildeling group"
    
    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith(".csv"):
                messages.warning(request, "Wrong file type was uploaded. Please upload a CSV file.")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for line in csv_data:
                fields = line.split(",")

                form_data = {
                    "first_name": fields[0],
                    "last_name": fields[1],
                    "username": fields[2],
                    "email": fields[3],
                    "phone": fields[4],
                    "team": fields[5],
                }

                # Generate a random password (you can customize the length and characters)
                random_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))
                form_data["password"] = random_password
                # Set date_joined to the current date and time
                form_data["date_joined"] = datetime.now()


                form = VolunteerAdminForm(form_data)
                
                # Check if user with the same email already exists
                existing_user = models.Volunteer.objects.filter(email=form_data["email"]).first()
                
                if existing_user:
                    # Delete existing TeamMembership and EventMembership objects where member is the user
                    try:
                        TeamMembership.objects.filter(member=existing_user).delete()
                        EventMembership.objects.filter(volunteer=existing_user).delete()
                    except Exception as e:
                        messages.warning(request, f"Error: {e}")

                    # Assign "Medarbejder" auth group
                    medarbejder_group, _ = Group.objects.get_or_create(name="Medarbejder")
                    existing_user.groups.add(medarbejder_group)

                    # Create TeamMembership for each team
                    team = Team.objects.get(id=form_data["team"])  # assuming team_id is the ID of the team
                    TeamMembership.objects.create(team=team, member=existing_user)
                    EventMembership.objects.create(volunteer=existing_user, event=Event.objects.filter(start_date__gte=date.today()).order_by('start_date').first())

                    messages.success(request, f"Updated: {existing_user.first_name} {existing_user.last_name} to {team.name} ")

                elif form.is_valid():
                    # Save the volunteer instance
                    volunteer = form.save()
                    print("volunteer", volunteer)

                    # Activate the user
                    User = get_user_model()  # Get the custom user model
                    user = User.objects.get(username=volunteer.username)
                    user.is_active = True
                    user.save()

                    # Assign "Medarbejder" auth group
                    medarbejder_group, _ = Group.objects.get_or_create(name="Medarbejder")
                    volunteer.groups.add(medarbejder_group)

                    # Create TeamMembership for each team
                    team = Team.objects.get(id=form_data["team"])  # assuming team_id is the ID of the team
                    TeamMembership.objects.create(team=team, member=volunteer)
                    EventMembership.objects.create(volunteer=volunteer, event=Event.objects.filter(start_date__gte=date.today()).order_by('start_date').first())


                    messages.success(request, f"Created: {user.first_name} {user.last_name} to {team.name} ")
                else:
                    error_messages = []
                    for field, errors in form.errors.items():
                        error_messages.append(f"Field '{field}': {'; '.join(map(str, errors))}")
                    error_message = "; ".join(error_messages)
                    messages.warning(request, f"Invalid data in CSV: {error_message}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
    
    
    def send_email_action(self, request, queryset):
        email_template = "organization/reset_password_guide_email.html"

        for volunteer in queryset:
            subject = "Velkommen til Seniorkursus Slettens booking system"
            first_team = volunteer.teams.first()  # Get the first team of the volunteer
            context = {'volunteer': volunteer,
                       'first_team': first_team}
            message = render_to_string(email_template, context)
            plain_message = strip_tags(message)

            send_mail(subject, plain_message, 'seniorkursussletten@gmail.com', [volunteer.email], html_message=message)
        
        self.message_user(request, f"Emails sent to {queryset.count()} volunteers.")
    send_email_action.short_description = "Send hjælp til at komme igang email til volunteers"

    def deactivate_volunteers(self, request, queryset):
        count = queryset.count()
        for volunteer in queryset:
            volunteer.is_active = False
            volunteer.save()

        self.message_user(
            request,
            ngettext(
                '%d volunteer was successfully deactivated.',
                '%d volunteers were successfully deactivated.',
                count,
            ) % count,
            messages.SUCCESS,
        )

    deactivate_volunteers.short_description = "Deactivate selected volunteers"

    def activate_volunteers(self, request, queryset):
        count = queryset.count()
        for volunteer in queryset:
            volunteer.is_active = True
            volunteer.save()

        self.message_user(
            request,
            ngettext(
                '%d volunteer was successfully activated.',
                '%d volunteers were successfully activated.',
                count,
            ) % count,
            messages.SUCCESS,
        )

    activate_volunteers.short_description = "Activate selected volunteers"

    def create_event_membership(modeladmin, request, queryset):
        # Get the next upcoming event
        next_event = Event.objects.filter(start_date__gte=date.today()).order_by('start_date').first()

        # Create EventMembership for selected volunteers with the next upcoming event
        for volunteer in queryset:
            EventMembership.objects.create(volunteer=volunteer, event=next_event)

        modeladmin.message_user(request, f'Event Memberships created for selected volunteers with the next upcoming event: {next_event}', level='success')

    create_event_membership.short_description = "Add selected to the next event"



    
        
        
class KeyAdminForm(forms.ModelForm):

    class Meta:
        model = models.Key
        fields = "__all__"


class KeyAdmin(admin.ModelAdmin):
    form = KeyAdminForm
    list_display = [
        "number",
        "name",
        "current_user",
        "description",
    ]
    readonly_fields = [
        "last_updated",
    ]



class TodoAdmin(admin.ModelAdmin):
    list_display = ['description', 'is_completed', 'user']



admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.TeamMembership, TeamMembershipAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventMembership, EventMembershipAdmin)
admin.site.register(models.Volunteer, VolunteerAdmin)
admin.site.register(models.Key, KeyAdmin)
admin.site.register(models.TeamEventMembership, TeamEventMembershipAdmin)
admin.site.register(models.Todo, TodoAdmin)