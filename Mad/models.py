from django.db import models
from django.urls import reverse


class MadItem(models.Model):

    # Relationships
    kategori = models.ForeignKey("Mad.MadKategori", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    indhold = models.DecimalField(max_digits=10, decimal_places=2)
    er_aktiv = models.BooleanField(default=True)
    enhed = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Mad_MadItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Mad_MadItem_update", args=(self.pk,))



class MadKategori(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    navn = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Mad_MadKategori_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Mad_MadKategori_update", args=(self.pk,))



class MadBooking(models.Model):

    # Fields
    aktivitet = models.CharField(max_length=30)
    forklaring = models.TextField(max_length=200)
    antal = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    anvendelses_tidspunkt = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Mad_MadBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Mad_MadBooking_update", args=(self.pk,))

