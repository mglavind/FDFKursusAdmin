from typing import List
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.urls.resolvers import URLPattern
from .models import Volunteer
import random
from datetime import datetime
import csv

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

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()




class VolunteerAdmin(admin.ModelAdmin):
    form = VolunteerAdminForm
    list_display = [
        "email",
        "phone",
        "first_name",
        "last_name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    actions = ["export_to_csv"]

    def export_to_csv(modeladmin, request, queryset):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="volunteers.csv"'

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
                    form.save()
                else:
                    error_messages = []
                    for field, errors in form.errors.items():
                        error_messages.append(f"Field '{field}': {'; '.join(map(str, errors))}")
                    error_message = "; ".join(error_messages)
                    messages.warning(request, f"Invalid data in CSV: {error_message}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
    
        
        


admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.TeamMembership, TeamMembershipAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventMembership, EventMembershipAdmin)
admin.site.register(models.Volunteer, VolunteerAdmin)