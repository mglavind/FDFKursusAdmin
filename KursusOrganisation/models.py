from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Medarbejder(models.Model):

    # Relationships
    #user = models.OneToOneField("settings.AUTH_USER_MODEL", on_delete=models.CASCADE)

    # Fields
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True)
    navn = models.CharField(max_length=30)
    telefon_nummer = models.CharField(max_length=8)
    medarbejder_email = models.EmailField(default="email@address.dummy")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("KursusOrganisation_Medarbejder_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("KursusOrganisation_Medarbejder_update", args=(self.pk,))



class Kursus(models.Model):

    # Fields
    start_date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    navn = models.CharField(max_length=30)
    end_date = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("KursusOrganisation_Kursus_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("KursusOrganisation_Kursus_update", args=(self.pk,))



class Team(models.Model):

    # Relationships
    medarbejder = models.ManyToManyField("KursusOrganisation.Medarbejder")
    kursus = models.ManyToManyField("KursusOrganisation.Kursus")

    # Fields
    last_updated = models.DateTimeField(auto_now=True)
    navn = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("KursusOrganisation_Team_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("KursusOrganisation_Team_update", args=(self.pk,))

