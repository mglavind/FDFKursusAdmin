from django.contrib import admin
from django import forms
from typing import List
from django import forms
from django.urls.resolvers import URLPattern
from django.contrib import admin, messages
from django.urls import path
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import SOSItem
from django.utils import formats
import csv

from . import models

class SOSBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.SOSBooking
        fields = "__all__"


class SOSBookingAdmin(admin.ModelAdmin):
    form = SOSBookingAdminForm

    list_max_show_all = 500  # Set the maximum number of items per page to 100
    list_per_page = 25  # Set the default number of items per page to 25
    # ...


    def formatted_team_contact(self, obj):
        return obj.team_contact.first_name

    formatted_team_contact.short_description = "Team Contact"

    def formatted_start_date(self, obj):
        formatted_date = obj.start.strftime("%d/%m")  # Format as DD/MM
        formatted_time = obj.start.strftime("%H:%M")  # Format as HH:MM
        return f"{formatted_date} - {formatted_time}"

    def formatted_end_date(self, obj):
        formatted_date = obj.end.strftime("%d/%m")  # Format as DD/MM
        formatted_time = obj.end.strftime("%H:%M")  # Format as HH:MM
        return f"{formatted_date} - {formatted_time}"

    formatted_start_date.short_description = "Start Date"
    formatted_end_date.short_description = "End Date"


    def formatted_last_updated(self, obj):
        formatted_date = obj.last_updated.strftime("%d/%m")  # Format as DD/MM
        formatted_time = obj.last_updated.strftime("%H:%M")  # Format as HH:MM
        return f"{formatted_date} - {formatted_time}"

    formatted_last_updated.short_description = "Last Updated"



    list_display = [
        "item",
        "status",
        "quantity",
        "team",
        "formatted_team_contact",
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
    actions = ["approve_bookings", "reject_bookings", "export_to_csv"]
    list_filter = (
        ('status', ChoiceDropdownFilter),
        ('item', RelatedDropdownFilter),
        ('team', RelatedDropdownFilter),
    )

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
        response["Content-Disposition"] = "attachment; filename=sos_bookings.csv"
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)
        writer.writerow(["Item", "Quantity","Remarks","Internal remarks", "Team", "Team Contact", "Start", "End", "Status", "Delivery needed", "Assistance needed"])

        for booking in queryset:
            writer.writerow([
                booking.item,
                booking.quantity,
                booking.remarks,
                booking.remarks_internal,
                booking.team,
                booking.team_contact,
                booking.start,
                booking.end,
                booking.status,
                booking.delivery_needed,
                booking.assistance_needed,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"



class SOSItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.SOSItem
        fields = "__all__"

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class SOSItemAdmin(admin.ModelAdmin):
    form = SOSItemAdminForm
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
                if SOSItem.objects.filter(name=name).exists():
                    messages.warning(request, f"Item with name '{name}' already exists.")
                    continue

                form_data = {
                    "name": name,
                    "description": description,
                }

                # Create a SOSItemAdminForm instance with the modified form_data
                form = SOSItemAdminForm(form_data)

                if form.is_valid():
                    # Save the SOSItem instance
                    sos_item = form.save()

                else:
                    error_messages = []
                    for field, errors in form.errors.items():
                        error_messages.append(f"Field '{field}': {'; '.join(map(str, errors))}")
                    error_message = "; ".join(error_messages)
                    messages.warning(request, f"Invalid data in CSV: {error_message}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

    



class SOSTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.SOSType
        fields = "__all__"


class SOSTypeAdmin(admin.ModelAdmin):
    form = SOSTypeAdminForm
    list_display = [
        "name",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.SOSBooking, SOSBookingAdmin)
admin.site.register(models.SOSItem, SOSItemAdmin)
admin.site.register(models.SOSType, SOSTypeAdmin)
