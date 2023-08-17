from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
import csv


from . import models


class ButikkenItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenItem
        fields = "__all__"


class ButikkenItemAdmin(admin.ModelAdmin):
    form = ButikkenItemAdminForm
    list_display = [
        "description",
        "last_updated",
        "name",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class ButikkenBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenBooking
        fields = "__all__"


class ButikkenBookingAdmin(admin.ModelAdmin):
    form = ButikkenBookingAdminForm
    list_display = [
        "remarks",
        "quantity",
        "created",
        "status",
        "last_updated",
        "start",
    ]
    readonly_fields = [
        "created",
        "last_updated",
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
        response["Content-Disposition"] = "attachment; filename=butikken_bookings.csv"

        writer = csv.writer(response)
        writer.writerow(["Item", "Quantity", "Team", "Team Contact", "Start", "Status"])

        for booking in queryset:
            writer.writerow([
                booking.item,
                booking.quantity,
                booking.team,
                booking.team_contact,
                booking.start,
                booking.status,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"


class ButikkenItemTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenItemType
        fields = "__all__"


class ButikkenItemTypeAdmin(admin.ModelAdmin):
    form = ButikkenItemTypeAdminForm
    list_display = [
        "last_updated",
        "name",
        "created",
        "description",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.ButikkenItem, ButikkenItemAdmin)
admin.site.register(models.ButikkenBooking, ButikkenBookingAdmin)
admin.site.register(models.ButikkenItemType, ButikkenItemTypeAdmin)
