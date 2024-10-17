from django import forms
from typing import List
from django.urls.resolvers import URLPattern
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from .models import ButikkenItem, MealBooking, Day, Meal, Recipe, Option, MealPlan, MealOption, TeamMealPlan
import csv
from django.contrib import admin
from django import forms


from . import models


class ButikkenItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenItem
        fields = "__all__"

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class ButikkenItemAdmin(admin.ModelAdmin):
    form = ButikkenItemAdminForm
    list_display = [
        "name",
        "description",
        "content_normal",
        "content_unit",
        "type",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    actions = ["export_to_csv"]
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
                content_normal = fields[2]
                content_unit = fields[3]
                type = fields[4]

                # Check if the name is unique
                if ButikkenItem.objects.filter(name=name).exists():
                    messages.warning(request, f"Item with name '{name}' already exists.")
                    continue

                form_data = {
                    "name": name,
                    "description": description,
                    "content_normal": content_normal,
                    "content_unit": content_unit,
                    "type": type,
                }

                # Create a LocationItemAdminForm instance with the modified form_data
                form = ButikkenItemAdminForm(form_data)

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
    

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=meal_items.csv"
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)
        writer.writerow([
            "name",
            "type",
            "content_normal",
            "content_unit",
            "description",
        ])

        for item in queryset:
            writer.writerow([
                item.name,
                item.type,
                item.content_normal,
                item.content_unit,
                item.description,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"
    








class ButikkenBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.ButikkenBooking
        fields = "__all__"


class ButikkenBookingAdmin(admin.ModelAdmin):
    form = ButikkenBookingAdminForm
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
        "team",
        "formatted_team_contact",
        "remarks",
        "quantity",
        "unit",
        "formatted_start_date",
        "status",
        "created",
        "formatted_last_updated",
        "remarks_internal",
        "for_meal",
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
    actions = ["approve_bookings", "reject_bookings", "udlever_bookings", "export_to_csv"]
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

    def udlever_bookings(self, request, queryset):
        for booking in queryset:
            booking.status = "Udleveret"
            booking.save()

        self.message_user(request, f"{queryset.count()} booking(s) udleveret.")
    udlever_bookings.short_description = "Booking udleveret"

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=butikken_bookings.csv"
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)
        writer.writerow(["Item", "Quantity", "Unit", "Team", "Team Contact", "Start", "start tid", "Status","Remarks","last updated", "remarks internal", "for meal"])

        for booking in queryset:
            writer.writerow([
                booking.item,
                booking.quantity,
                booking.unit,
                booking.team,
                booking.team_contact,
                booking.start,
                booking.start_time,
                booking.status,
                booking.remarks,
                booking.last_updated,
                booking.remarks_internal,
                booking.for_meal,
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



class DayAdminForm(forms.ModelForm):

    class Meta:
        model = models.Day
        fields = "__all__"


class DayAdmin(admin.ModelAdmin):
    form = DayAdminForm
    list_display = [
        "name",
        "last_updated",
        "created",
        "date",
    ]
    readonly_fields = [
        "name",
        "last_updated",
        "created",
        "date",
    ]


class RecipeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Recipe
        fields = "__all__"


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
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

class MealAdminForm(forms.ModelForm):

    class Meta:
        model = models.Meal
        fields = "__all__"


class MealAdmin(admin.ModelAdmin):
    form = MealAdminForm
    list_display = [
        "created",
        "type",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "type",
        "last_updated",
    ]


class OptionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Option
        fields = "__all__"


class OptionAdmin(admin.ModelAdmin):
    form = OptionAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
class MealBookingAdminForm(forms.ModelForm):

    class Meta:
        model = models.MealBooking
        fields = "__all__"


class MealBookingAdmin(admin.ModelAdmin):
    form = MealBookingAdminForm
    list_display = [
        "team",
        "last_updated",
        "created",
        "status",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    list_filter = ["team", "status"]
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
        response["Content-Disposition"] = "attachment; filename=meal_bookings.csv"
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)
        writer.writerow([
            "team",
            "last_updated",
            "created",
            "status",
        ])

        for booking in queryset:
            writer.writerow([
                booking.team,
                booking.last_updated,
                booking.created,
                booking.status,
            ])

        return response
    export_to_csv.short_description = "Export selected bookings to CSV"

class MealPlanAdminForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = "__all__"


class MealPlanInline(admin.TabularInline):
    model = MealOption
    extra = 1


class MealPlanAdmin(admin.ModelAdmin):
    form = MealPlanAdminForm
    list_display = [
        "name",
        "get_day_of_week",  # Add the new field here
        "meal_date",
        "open_date",
        "close_date",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    inlines = [
        MealPlanInline,
    ]

    def get_day_of_week(self, obj):
        return obj.meal_date.strftime("%A")  # Return the friendly name for the day

    get_day_of_week.short_description = "Day of Week"  # Set the column header for the new field


class MealOptionAdminForm(forms.ModelForm):
    class Meta:
        model = MealOption
        fields = "__all__"

class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 0

    
class MealOptionAdmin(admin.ModelAdmin):
    form = MealOptionAdminForm
    list_display = [
        "meal_plan",
        "recipe",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]

class TeamMealPlanAdminForm(forms.ModelForm):
    class Meta:
        model = TeamMealPlan
        fields = "__all__"

class TeamMealPlanAdmin(admin.ModelAdmin):
    form = TeamMealPlanAdminForm
    list_display = [
        "team",
        "meal_plan",
        "meal_option",
        "team_contact",
        "status",
        "last_updated",
        "created",
        
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    actions = ["approve_bookings", "reject_bookings", "export_to_csv"]

    def approve_bookings(self, request, queryset):
        for booking in queryset:
            booking.status = "Approved"
            booking.save()

        self.message_user(request, f"{queryset.count()} booking(s) approved.")
    approve_bookings.short_description = "Godkend valgte"

    def reject_bookings(self, request, queryset):
        for booking in queryset:
            booking.status = "Rejected"
            booking.save()

        self.message_user(request, f"{queryset.count()} booking(s) rejected.")
    reject_bookings.short_description = "Afvis valgte"

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=meal_bookings.csv"
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)
        writer.writerow([
            "Team",
            "Måltid",
            "Måltidspakke",
            "Kontaktperson",
            "Status",
            "last_updated",
            "created",
        ])

        for booking in queryset:
            writer.writerow([
                booking.team,
                booking.meal_plan,
                booking.meal_option,
                booking.team_contact,
                booking.status,
                booking.last_updated,
                booking.created,
            ])

        return response
    export_to_csv.short_description = "Eksporter valgte til CSV"





admin.site.register(models.TeamMealPlan, TeamMealPlanAdmin)
admin.site.register(models.MealPlan, MealPlanAdmin)
admin.site.register(models.MealOption, MealOptionAdmin)
#admin.site.register(models.Day, DayAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
#admin.site.register(models.ButikkenItemType, ButikkenItemTypeAdmin)
#admin.site.register(models.Meal, MealAdmin)
#admin.site.register(models.Option, OptionAdmin)
admin.site.register(models.ButikkenItem, ButikkenItemAdmin)
admin.site.register(models.ButikkenBooking, ButikkenBookingAdmin)
#admin.site.register(models.MealBooking, MealBookingAdmin)
