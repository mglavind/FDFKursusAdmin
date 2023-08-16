from django.contrib import admin
from django import forms

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


class SjakBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.SjakBooking
        fields = "__all__"


class SjakBookingAdmin(admin.ModelAdmin):
    form = SjakBookingAdminForm
    list_display = [
        "remarks",
        "last_updated",
        "created",
        "status",
        "quantity",
        "use_date",
        "item",
        "team",
        "team_contact",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        
    ]


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
