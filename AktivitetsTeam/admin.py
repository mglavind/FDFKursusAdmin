from django.contrib import admin
from django import forms
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.http import HttpResponseRedirect, HttpResponse
import csv

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
    list_filter = (
        ('status', ChoiceDropdownFilter),
        ('item', RelatedDropdownFilter),
        ('team', RelatedDropdownFilter),
    )
    actions = ["approve_bookings", "reject_bookings", "export_to_csv"]
    search_fields = ['item__name', 'team__name'] 

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
        
        writer.writerow(["Item", "Quantity", "Team", "Team Contact", "Start", "End", "Status", "Remarks", "Internal remarks"])

        for booking in queryset:
            writer.writerow([
                booking.item,
                booking.quantity,
                booking.team,
                booking.team_contact,
                booking.start,
                booking.end,
                booking.status,
                booking.remarks,
                booking.remarks_internal,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"




admin.site.register(models.AktivitetsTeamItem, AktivitetsTeamItemAdmin)
admin.site.register(models.AktivitetsTeamBooking, AktivitetsTeamBookingAdmin)
