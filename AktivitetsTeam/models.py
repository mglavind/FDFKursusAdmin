from django.db import models
from django.urls import reverse


class AktivitetsTeamItem(models.Model):

    # Fields
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("AktivitetsTeam_AktivitetsTeamItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("AktivitetsTeam_AktivitetsTeamItem_update", args=(self.pk,))



class AktivitetsTeamBooking(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("AktivitetsTeam.AktivitetsTeamItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)


    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Fields
    location = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True)  # Blank allows for an empty value

   

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("AktivitetsTeam_AktivitetsTeamBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("AktivitetsTeam_AktivitetsTeamBooking_update", args=(self.pk,))
    
    def approve_bookings(self, request, queryset):
        queryset.update(status="Approved")

    approve_bookings.short_description = "Approve selected bookings"

    def reject_bookings(self, request, queryset):
        queryset.update(status="Rejected")

    reject_bookings.short_description = "Rejected selected bookings"

