from typing import List
from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.urls import path
from django.shortcuts import render
from organization.models import Team, TeamMembership, TeamEventMembership, EventMembership, Event
from django.db.models import Min
from datetime import date
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.urls.resolvers import URLPattern
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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

class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    #inlines = [TeamEventMembershipInline]
    list_display = [
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




class VolunteerAdmin(admin.ModelAdmin):
    form = VolunteerAdminForm
    inlines = [EventMembershipInline]
    list_display = [
        "first_name",
        "last_name",
        "username",
        "email",
        "phone",
        "display_events",
        "created",
        "last_updated",
        "is_active",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    actions = ["export_to_csv", "send_email_action", "deactivate_volunteers", "activate_volunteers", "create_event_membership"]

    def display_events(self, obj):
        return ", ".join([event.name for event in obj.events.all()])
    
    def export_to_csv(modeladmin, request, queryset):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="volunteers.csv"'
            response.write(u'\ufeff'.encode('utf8'))

            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Username', 'Email', 'Phone'])

            for volunteer in queryset:
                writer.writerow([volunteer.first_name, volunteer.last_name, volunteer.username, volunteer.email, volunteer.phone])
            return response
    export_to_csv.short_description = "Export selected volunteers to CSV"
    
    def get_urls(self) -> List[URLPattern]:
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
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
                }
                
                # Generate a random password (you can customize the length and characters)
                random_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))
                form_data["password"] = random_password
                
                # Set date_joined to the current date and time
                form_data["date_joined"] = datetime.now()

                # Create a VolunteerAdminForm instance with the modified form_data
                form = VolunteerAdminForm(form_data)

                if form.is_valid():
                     # Save the volunteer instance
                    volunteer = form.save()

                     # Activate the user
                    User = get_user_model()  # Get the custom user model
                    user = User.objects.get(username=volunteer.username)
                    user.is_active = True
                    user.save()

                    # Create TeamMembership for the "Unassigned" team
                    unassigned_team = Team.objects.get(name="Unassigned users")
                    team_membership = TeamMembership.objects.create(team=unassigned_team, member=volunteer)

                    # Assign "Medarbejder" auth group
                    medarbejder_group, _ = Group.objects.get_or_create(name="Medarbejder")
                    volunteer.groups.add(medarbejder_group)
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
            context = {'volunteer': volunteer}
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