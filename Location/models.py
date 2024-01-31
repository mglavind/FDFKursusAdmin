from django.db import models
from django.urls import reverse
import datetime

class LocationType(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=500)
    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Location_LocationType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Location_LocationType_update", args=(self.pk,))



class LocationBooking(models.Model):

    # Relationships
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)
    item = models.ForeignKey("Location.LocationItem", on_delete=models.CASCADE)
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Fields

    start_date = models.DateField(default=datetime.datetime.now)
    start_time = models.TimeField(default=datetime.time(8, 0))
    end_date = models.DateField(default=datetime.datetime.now)
    end_time = models.TimeField(default=datetime.time(8, 0))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True)  # Blank allows for an empty value
    created = models.DateTimeField(auto_now_add=True, editable=False)
    primary_camp = models.BooleanField(default=False, blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Location_LocationBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Location_LocationBooking_update", args=(self.pk,))
    def approve_bookings(self, request, queryset):
        queryset.update(status="Approved")

    approve_bookings.short_description = "Approve selected bookings"

    def reject_bookings(self, request, queryset):
        queryset.update(status="Rejected")

    reject_bookings.short_description = "Rejected selected bookings"



class LocationItem(models.Model):

    # Relationships
    type = models.CharField(max_length=200, blank=True)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Location_LocationItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Location_LocationItem_update", args=(self.pk,))

