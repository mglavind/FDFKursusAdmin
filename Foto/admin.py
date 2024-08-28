from django.contrib import admin
from django import forms
from icalendar import Calendar, Event
from django.http import HttpResponseRedirect, HttpResponse
from . import models


class FotoItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.FotoItem
        fields = "__all__"


class FotoItemAdmin(admin.ModelAdmin):
    form = FotoItemAdminForm
    list_display = [
        "name",
        "description",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class FotoBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.FotoBooking
        fields = "__all__"


class FotoBookingAdmin(admin.ModelAdmin):
    form = FotoBookingAdminForm
    list_display = [
        "item",
        "location",
        "start_time",
        "end_time",
        "start_date",
        "end_date",
        "remarks",
        "status",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    actions = ["approve_bookings", "reject_bookings"]
    list_filter = ["item", "team", "status"]

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

    def export_selected_to_ical(self, request, queryset):
        calendar = Calendar()

        def convert_to_ical(booking):
            ical_event = Event()
            summary = f"{booking.item} - {booking.team} - {booking.team_contact}"
            ical_event.add('summary', summary)
            ical_event.add('dtstart', booking.start_date)
            ical_event.add('dtend', booking.end_date)
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

    export_selected_to_ical.short_description = "Export selected bookings to iCal"


admin.site.register(models.FotoItem, FotoItemAdmin)
admin.site.register(models.FotoBooking, FotoBookingAdmin)
