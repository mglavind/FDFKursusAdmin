from django.db import models
from django.urls import reverse


class ButikkenItem(models.Model):

    # Relationships
    type = models.ForeignKey("Butikken.ButikkenItemType", on_delete=models.CASCADE)

    # Fields
    description = models.TextField(max_length=500)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Butikken_ButikkenItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_ButikkenItem_update", args=(self.pk,))



class ButikkenBooking(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("Butikken.ButikkenItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    # Fields
    remarks = models.TextField(max_length=500)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    start = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Butikken_ButikkenBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_ButikkenBooking_update", args=(self.pk,))



class ButikkenItemType(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Butikken_ButikkenItemType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_ButikkenItemType_update", args=(self.pk,))

