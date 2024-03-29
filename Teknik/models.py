from django.db import models
from django.contrib.auth.models import Group
from django.urls import reverse
import datetime

class TeknikBooking(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("Teknik.TeknikItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Fields
    start = models.DateTimeField(default=datetime.datetime.now)
    end = models.DateTimeField(default=datetime.datetime.now)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True)  # Blank allows for an empty value
    remarks_internal = models.TextField(blank=True)  # Blank allows for an empty value
    assistance_needed = models.BooleanField(default=False, blank=True)
    delivery_needed = models.BooleanField(default=False, blank=True)



    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Teknik_TeknikBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Teknik_TeknikBooking_update", args=(self.pk,))
    
    def approve_bookings(self, request, queryset):
        queryset.update(status="Approved")

    approve_bookings.short_description = "Approve selected bookings"

    def reject_bookings(self, request, queryset):
        queryset.update(status="Rejected")

    reject_bookings.short_description = "Rejected selected bookings"



class TeknikItem(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Teknik_TeknikItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Teknik_TeknikItem_update", args=(self.pk,))



class TeknikType(models.Model):

    # Fields
    name = models.CharField(max_length=30, null=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False, null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Teknik_TeknikType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Teknik_TeknikType_update", args=(self.pk,))

