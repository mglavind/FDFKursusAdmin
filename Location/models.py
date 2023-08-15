from django.db import models
from django.urls import reverse


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

    # Fields
    end = models.DateTimeField()
    status = models.CharField(max_length=30)
    remarks = models.TextField(max_length=500)
    start = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    primary_camp = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Location_LocationBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Location_LocationBooking_update", args=(self.pk,))



class LocationItem(models.Model):

    # Relationships
    type = models.ForeignKey("Location.LocationType", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Location_LocationItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Location_LocationItem_update", args=(self.pk,))

