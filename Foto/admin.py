from django.contrib import admin
from django import forms

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
        "start",
        "end",
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


admin.site.register(models.FotoItem, FotoItemAdmin)
admin.site.register(models.FotoBooking, FotoBookingAdmin)
