from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone


class SjakItem(models.Model):

    # Relationships
    type = models.ForeignKey("Sjak.SjakItemType", on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Sjak_SjakItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Sjak_SjakItem_update", args=(self.pk,))



class SjakBooking(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("Sjak.SjakItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)
       
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Fields
    start = models.DateTimeField(verbose_name='Start', default=timezone.now)
    end = models.DateTimeField(verbose_name='End', default=timezone.now)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True)  # Blank allows for an empty value
    remarks_internal = models.TextField(blank=True)  # Blank allows for an empty value

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Sjak_SjakBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Sjak_SjakBooking_update", args=(self.pk,))
    
    def approve_bookings(self, request, queryset):
        queryset.update(status="Approved")

    approve_bookings.short_description = "Approve selected bookings"

    def reject_bookings(self, request, queryset):
        queryset.update(status="Rejected")

    reject_bookings.short_description = "Rejected selected bookings"



class SjakItemType(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Sjak_SjakItemType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Sjak_SjakItemType_update", args=(self.pk,))

