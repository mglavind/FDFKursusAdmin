from django.contrib import admin
from django import forms
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import formats
from icalendar import Calendar, Event
from datetime import datetime
import csv

from . import models
from .models import AktivitetsTeamBooking


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

class AssignedInline(admin.TabularInline):
        model = AktivitetsTeamBooking.assigned_aktivitetsteam.through

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
        ('assigned_aktivitetsteam', RelatedDropdownFilter)
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
