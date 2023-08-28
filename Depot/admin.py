from django.contrib import admin
from django import forms
from typing import List
from django import forms
from django.urls.resolvers import URLPattern
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from .models import DepotItem
import csv


from . import models


class DepotItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotItem
        fields = "__all__"

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class DepotItemAdmin(admin.ModelAdmin):
    form = DepotItemAdminForm
    list_display = [
        "name",
        "description",
        "unit",
        "quantity_lager",
        "box",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "last_updated",
        "description",
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
                unit = fields[2]
                quantity_lager = fields[3]
                box = fields[4]

                # Check if the name is unique
                if DepotItem.objects.filter(name=name).exists():
                    messages.warning(request, f"Item with name '{name}' already exists.")
                    continue

                form_data = {
                    "name": name,
                    "description": description,
                    "unit": unit,
                    "quantity_lager": quantity_lager,
                    "box": box,
                }

                # Create a LocationItemAdminForm instance with the modified form_data
                form = DepotItemAdminForm(form_data)

                if form.is_valid():
                    # Save the LocationItem instance
                    location_item = form.save()

                else:
                    error_messages = []
                    for field, errors in form.errors.items():
                        error_messages.append(f"Field '{field}': {'; '.join(map(str, errors))}")
                    error_message = "; ".join(error_messages)
                    messages.warning(request, f"Invalid data in CSV: {error_message}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class DepotLocationAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotLocation
        fields = "__all__"


class DepotLocationAdmin(admin.ModelAdmin):
    form = DepotLocationAdminForm
    list_display = [
        "name",
        "description",
        "address",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class DepotBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotBooking
        fields = "__all__"


class DepotBookingAdmin(admin.ModelAdmin):
    form = DepotBookingAdminForm
    list_display = [
        "item",
        "quantity",
        "team",
        "team_contact",
        "remarks",
        "start",
        "end",
        "status",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    list_filter = (
        ('status', ChoiceDropdownFilter),
        ('item', RelatedDropdownFilter),
        ('team', RelatedDropdownFilter),
    )
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
        response["Content-Disposition"] = "attachment; filename=depot_bookings.csv"

        writer = csv.writer(response)
        writer.writerow(["Item", "Team", "Team Contact", "Start", "End", "Status"])

        for booking in queryset:
            writer.writerow([
                booking.item,
                booking.team,
                booking.team_contact,
                booking.start,
                booking.end,
                booking.status,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"






class DepotBoxAdminForm(forms.ModelForm):

    class Meta:
        model = models.DepotBox
        fields = "__all__"


class DepotBoxAdmin(admin.ModelAdmin):
    form = DepotBoxAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
        "description",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.DepotItem, DepotItemAdmin)
admin.site.register(models.DepotLocation, DepotLocationAdmin)
admin.site.register(models.DepotBooking, DepotBookingAdmin)
admin.site.register(models.DepotBox, DepotBoxAdmin)
