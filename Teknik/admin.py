from django.contrib import admin
from django import forms

from . import models

class TeknikBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeknikBooking
        fields = "__all__"


class TeknikBookingAdmin(admin.ModelAdmin):
    form = TeknikBookingAdminForm
    list_display = [
        "item",
        "status",
        "quantity",
        "team",
        "team_contact",
        "start",
        "end",
        "remarks",
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



class TeknikItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeknikItem
        fields = "__all__"


class TeknikItemAdmin(admin.ModelAdmin):
    form = TeknikItemAdminForm
    list_display = [
        "name",
        "last_updated",
        "created",
        "description",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class TeknikTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.TeknikType
        fields = "__all__"


class TeknikTypeAdmin(admin.ModelAdmin):
    form = TeknikTypeAdminForm
    list_display = [
        "name",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.TeknikBooking, TeknikBookingAdmin)
admin.site.register(models.TeknikItem, TeknikItemAdmin)
admin.site.register(models.TeknikType, TeknikTypeAdmin)
