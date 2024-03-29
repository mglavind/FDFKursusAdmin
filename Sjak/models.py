from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone

from organization.models import Event

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


class SjakItem(models.Model):

    # Relationships
    #type = models.CharField(max_length=100, blank=True)
    item_type = models.ForeignKey("Sjak.SjakItemType", default=1, blank=True, on_delete=models.CASCADE)


   
    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    quantity_lager = models.CharField(max_length=100, blank=True)
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
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
       
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    INTERNAL_STATUS_CHOICES = (
        ('Afventer', 'Afventer'),
        ('Igang', 'Igang'),
        ('Klar', 'Klar'),
        ('Afsluttet', 'Afsluttet'),
    )

    # Fields
    start = models.DateTimeField(verbose_name='Start dato')
    start_time = models.TimeField(verbose_name='Start tidspunkt', default='12:00')
    end = models.DateTimeField(verbose_name='Slut dato')
    end_time = models.TimeField(verbose_name='Slut tidspunkt', default='12:00')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True)  # Blank allows for an empty value
    remarks_internal = models.TextField(blank=True)  # Blank allows for an empty value
    status_internal = models.CharField(max_length=10, choices=INTERNAL_STATUS_CHOICES, default='Afventer')
    


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




