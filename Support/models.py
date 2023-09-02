from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone


class SupportItem(models.Model):

    # Relationships
    type = models.ForeignKey("Support.SupportItemType", on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Support_SupportItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Support_SupportItem_update", args=(self.pk,))



class SupportBooking(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("Support.SupportItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)
       
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Fields
    start = models.DateTimeField(verbose_name='Start', default=timezone.now)
    end = models.DateTimeField(verbose_name='End', default=timezone.now)

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
        return reverse("Support_SupportBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Support_SupportBooking_update", args=(self.pk,))
    
    def approve_bookings(self, request, queryset):
        queryset.update(status="Approved")

    approve_bookings.short_description = "Approve selected bookings"

    def reject_bookings(self, request, queryset):
        queryset.update(status="Rejected")

    reject_bookings.short_description = "Rejected selected bookings"



class SupportItemType(models.Model):

    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Support_SupportItemType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Support_SupportItemType_update", args=(self.pk,))

