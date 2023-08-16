from django.contrib import admin
from django import forms

from . import models


class LocationTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.LocationType
        fields = "__all__"


class LocationTypeAdmin(admin.ModelAdmin):
    form = LocationTypeAdminForm
    list_display = [
        "created",
        "last_updated",
        "description",
        "name",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
   


class LocationBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.LocationBooking
        fields = "__all__"


class LocationBookingAdmin(admin.ModelAdmin):
    form = LocationBookingAdminForm
    list_display = [
        "end",
        "status",
        "remarks",
        "start",
        "created",
        "primary_camp",
        "last_updated",
        "item",
        "team",
        "team_contact",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    actions = ["approve_bookings", "reject_bookings"]

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


class LocationItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.LocationItem
        fields = "__all__"


class LocationItemAdmin(admin.ModelAdmin):
    form = LocationItemAdminForm
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


admin.site.register(models.LocationType, LocationTypeAdmin)
admin.site.register(models.LocationBooking, LocationBookingAdmin)
admin.site.register(models.LocationItem, LocationItemAdmin)
