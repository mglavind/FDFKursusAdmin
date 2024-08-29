from django.contrib import admin, messages
from django import forms
from django.db.models import Q
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import formats
from organization.models import Volunteer
from icalendar import Calendar, Event
from datetime import datetime
from django.contrib.admin import SimpleListFilter
from geopy.geocoders import Nominatim
from django.urls import path, URLPattern
from django.shortcuts import render
from typing import List
import csv

from . import models
from .models import AktivitetsTeamBooking


class AktivitetsTeamItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.AktivitetsTeamItem
        fields = "__all__"

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class AktivitetsTeamItemAdmin(admin.ModelAdmin):
    form = AktivitetsTeamItemAdminForm
    list_display = [
        "name",
        "description",
        "youtube_link",
        "description_aktiverede",
        "description_eksempel",
        "description_flow",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    search_fields = ['name', 'description']
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=aktivitetsteam_items.csv"
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow([
            "name",
            "description",
            "short_description",
            "youtube_link",
            "description_aktiverede",
            "description_eksempel",
            "description_flow",
        ])

        for booking in queryset:
            writer.writerow([
                booking.name,
                booking.description,
                booking.short_description,
                booking.youtube_link,
                booking.description_aktiverede,
                booking.description_eksempel,
                booking.description_flow,
            ])

        return response
    export_to_csv.short_description = "Eksporter valgte til CSV"

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
                fields = line.split(";")
                name = fields[0]
                description = fields[1]
                short_description = fields[2]
                youtube_link = fields[3]
                description_aktiverede = fields[4]
                description_eksempel = fields[5]
                description_flow = fields[6]

                # Check if the name is unique
                if models.AktivitetsTeamItem.objects.filter(name=name).exists():
                    messages.warning(request, f"Item with name '{name}' already exists.")
                    continue

                form_data = {
                    "name": name,
                    "description": description,
                    "short_description": short_description,
                    "youtube_link": youtube_link,
                    "description_aktiverede": description_aktiverede,
                    "description_eksempel": description_eksempel,
                    "description_flow": description_flow,
                }

                # Create a LocationItemAdminForm instance with the modified form_data
                form = AktivitetsTeamItemAdminForm(form_data)

                if form.is_valid():
                    # Save the LocationItem instance
                    location_item = form.save()

                else:
                    error_messages = []
                    for field, errors in form.errors.items():
                        error_messages.append(f"Field '{field}': {'; '.join(map(str, errors))}")
                    error_message = "; ".join(error_messages)
                    messages.warning(request, f"Invalid data in CSV: {error_message}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class AktivitetsTeamBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.AktivitetsTeamBooking
        fields = "__all__"

class AssignedInline(admin.TabularInline):
    model = models.AktivitetsTeamBooking.assigned_aktivitetsteam.through
    verbose_name = "Tilknyttedet Aktivitettøs"
    verbose_name_plural = "Tilknyttede Aktivitettøser"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "volunteer":
            kwargs["queryset"] = Volunteer.objects.filter(teams='8')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class AssignedAktivitetsteamFilter(SimpleListFilter):
    title = 'Assigned Aktivitetsteam'
    parameter_name = 'assigned_aktivitetsteam'

    def lookups(self, request, model_admin):
        # Provide the filter options
        volunteers = Volunteer.objects.filter(teams='8')
        return [(volunteer.id, volunteer.first_name) for volunteer in volunteers]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(assigned_aktivitetsteam__id=self.value())
        return queryset

class AktivitetsTeamBookingAdmin(admin.ModelAdmin):
    form = AktivitetsTeamBookingAdminForm
    list_max_show_all = 500  # Set the maximum number of items per page to 100
    list_per_page = 25  # Set the default number of items per page to 25
    # ...


    def formatted_team_contact(self, obj):
        return obj.team_contact.first_name

    formatted_team_contact.short_description = "Team Contact"

    def formatted_start_date(self, obj):
        formatted_date = obj.start.strftime("%d/%m")  # Format as DD/MM
        formatted_time = obj.start.strftime("%H:%M")  # Format as HH:MM
        return f"{formatted_date} - {formatted_time}"

    def formatted_end_date(self, obj):
        formatted_date = obj.end.strftime("%d/%m")  # Format as DD/MM
        formatted_time = obj.end.strftime("%H:%M")  # Format as HH:MM
        return f"{formatted_date} - {formatted_time}"

    formatted_start_date.short_description = "Start Date"
    formatted_end_date.short_description = "End Date"


    def formatted_last_updated(self, obj):
        formatted_date = obj.last_updated.strftime("%d/%m")  # Format as DD/MM
        formatted_time = obj.last_updated.strftime("%H:%M")  # Format as HH:MM
        return f"{formatted_date} - {formatted_time}"

    formatted_last_updated.short_description = "Last Updated"

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
    list_filter = (
        ('status', ChoiceDropdownFilter),
        ('item', RelatedDropdownFilter),
        ('team', RelatedDropdownFilter),
        AssignedAktivitetsteamFilter,
    )
    actions = ["approve_bookings", "reject_bookings", "export_to_csv", "export_selected_to_ical"]
    search_fields = ['item__name', 'team__name'] 

    inlines = [
        AssignedInline,
    ]
    exclude = ["members"]
    

    def approve_bookings(self, request, queryset):
        for booking in queryset:
            booking.status = "Approved"
            booking.save()

        self.message_user(request, f"{queryset.count()} booking(s) approved.")
    approve_bookings.short_description = "Approve selected bookings"

    def reject_bookings(self, request, queryset):
        for booking in queryset:
            booking.status = "Rejected"
            booking.save()

        self.message_user(request, f"{queryset.count()} booking(s) rejected.")
    reject_bookings.short_description = "Reject selected bookings"

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=aktivitetsteam_bookings.csv"
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)
        
        writer.writerow(["Aktivitet", "Team", "Kontaktperson", "Start dato","Start tid", "Slut dato", "Slut tid", "location", "Status", "Remarks", "Assigned AT", "Internal remarks"])

        for booking in queryset:
            writer.writerow([
                booking.item,
                booking.team,
                booking.team_contact,
                booking.start_date,
                booking.start_time,
                booking.end_date,
                booking.end_time,
                booking.location,
                booking.status,
                booking.remarks,
                booking.assigned_aktivitetsteam,
                booking.remarks_internal,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"

        # Override the save_model method to add geolocation logic
    def save_model(self, request, obj, form, change):
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
        geolocator = Nominatim(user_agent="SKSBooking/1.0 (slettenbooking@gmail.com)")
        location = geolocator.reverse((latitude, longitude))
        if location:
            obj.address = location.address
        obj.save()

    # Override the change_view method to add map context
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        object = self.get_object(request, object_id)
        extra_context['latitude'] = object.latitude if object.latitude is not None else 56.1145
        extra_context['longitude'] = object.longitude if object.longitude is not None else 9.66427
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
   





    def export_selected_to_ical(self, request, queryset):
        calendar = Calendar()

        def convert_to_ical(booking):
            ical_event = Event()
            summary = f"{booking.item} - {booking.team} - {booking.team_contact}"
            ical_event.add('summary', summary)

            # Wrap date and time fields into datetime objects
            start_datetime = datetime.combine(booking.start_date, booking.start_time)
            end_datetime = datetime.combine(booking.end_date, booking.end_time)

            ical_event.add('dtstart', start_datetime)
            ical_event.add('dtend', end_datetime)
            ical_event.add('description', booking.remarks)

            # Add more properties as needed

            # Add the team_contact name in the "description" field
            description_with_contact = f"Kontaktperson: {booking.team_contact}\n{booking.remarks}"
            ical_event.add('description', description_with_contact)

            return ical_event

        for booking in queryset:
            ical_event = convert_to_ical(booking)
            calendar.add_component(ical_event)

        response = HttpResponse(calendar.to_ical(), content_type='text/calendar')
        response['Content-Disposition'] = 'attachment; filename="bookings.ics"'

        return response




admin.site.register(models.AktivitetsTeamItem, AktivitetsTeamItemAdmin)
admin.site.register(models.AktivitetsTeamBooking, AktivitetsTeamBookingAdmin)
