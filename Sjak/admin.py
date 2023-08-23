from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
import csv

from . import models


class SjakItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.SjakItem
        fields = "__all__"


class SjakItemAdmin(admin.ModelAdmin):
    form = SjakItemAdminForm
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
    


class SjakBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.SjakBooking
        fields = "__all__"


class SjakBookingAdmin(admin.ModelAdmin):
    form = SjakBookingAdminForm
    list_display = [
        "item",
        "quantity",
        "team",
        "team_contact",
        "start",
        "end",
        "status",
        "last_updated",
        "remarks",
        "remarks_internal",
        
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    list_filter = ["item", "team", "status"]
    actions = ["approve_bookings", "reject_bookings", "export_to_csv"]

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
        response["Content-Disposition"] = "attachment; filename=sjak_bookings.csv"

        writer = csv.writer(response)
        writer.writerow(["Item", "Quantity", "Team", "Team Contact", "Start", "End", "Status"])

        for booking in queryset:
            writer.writerow([
                booking.item,
                booking.quantity,
                booking.team,
                booking.team_contact,
                booking.start,
                booking.end,
                booking.status,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"


class SjakItemTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.SjakItemType
        fields = "__all__"


class SjakItemTypeAdmin(admin.ModelAdmin):
    form = SjakItemTypeAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.SjakItem, SjakItemAdmin)
admin.site.register(models.SjakBooking, SjakBookingAdmin)
admin.site.register(models.SjakItemType, SjakItemTypeAdmin)
