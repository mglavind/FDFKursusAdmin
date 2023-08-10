from django.db import models
from django.urls import reverse


class TeknikBooking(models.Model):

    # Relationships
    team_b = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item_b = models.ForeignKey("Teknik.TeknikItem", on_delete=models.CASCADE)
    team_contact_b = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    

    # Fields
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    end = models.DateTimeField()
    start = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=30)


    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Teknik_TeknikBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Teknik_TeknikBooking_update", args=(self.pk,))



class TeknikItem(models.Model):

    # Relationships
    owner = models.ForeignKey("auth.Group", on_delete=models.CASCADE)
    type = models.ForeignKey("Teknik.TeknikType", on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="upload/images/")
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
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Teknik_TeknikType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Teknik_TeknikType_update", args=(self.pk,))

