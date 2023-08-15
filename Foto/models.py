from django.db import models
from django.urls import reverse


class FotoItem(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Foto_FotoItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Foto_FotoItem_update", args=(self.pk,))



class FotoBooking(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("Foto.FotoItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    # Fields
    start = models.DateTimeField()
    end = models.DateTimeField()
    remarks = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Foto_FotoBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Foto_FotoBooking_update", args=(self.pk,))

