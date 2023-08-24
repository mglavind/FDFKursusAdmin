from django.contrib import admin
from django import forms
from typing import List
from django import forms
from django.urls.resolvers import URLPattern
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TeknikItem
import csv

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
        "remarks_internal",
        "created",
        "last_updated",
        "assistance_needed",
        "delivery_needed",
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

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


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
                fields = line.split(",")
                name = fields[0]
                description = fields[1]

                # Check if the name is unique
                if TeknikItem.objects.filter(name=name).exists():
                    messages.warning(request, f"Item with name '{name}' already exists.")
                    continue

                form_data = {
                    "name": name,
                    "description": description,
                }

                # Create a TeknikItemAdminForm instance with the modified form_data
                form = TeknikItemAdminForm(form_data)

                if form.is_valid():
                    # Save the TeknikItem instance
                    teknik_item = form.save()

                else:
                    error_messages = []
                    for field, errors in form.errors.items():
                        error_messages.append(f"Field '{field}': {'; '.join(map(str, errors))}")
                    error_message = "; ".join(error_messages)
                    messages.warning(request, f"Invalid data in CSV: {error_message}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

    



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
