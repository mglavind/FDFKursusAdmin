from django.db import models
from django.urls import reverse


class DepotItem(models.Model):

    # Relationships
    box = models.TextField(max_length=500)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, blank=True)
    quantity_lager = models.CharField(max_length=100, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Depot_DepotItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Depot_DepotItem_update", args=(self.pk,))



class DepotLocation(models.Model):

    # Fields
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Depot_DepotLocation_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Depot_DepotLocation_update", args=(self.pk,))



class DepotBooking(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("Depot.DepotItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Fields
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    # Fields
    remarks = models.TextField(max_length=500, blank=True)
    end = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    start = models.DateTimeField()
    quantity = models.BigIntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Depot_DepotBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Depot_DepotBooking_update", args=(self.pk,))



class DepotBox(models.Model):

    # Relationships
    location = models.ForeignKey("Depot.DepotLocation", on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Depot_DepotBox_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Depot_DepotBox_update", args=(self.pk,))

