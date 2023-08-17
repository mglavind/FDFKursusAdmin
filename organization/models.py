from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Volunteer(AbstractUser):

    # Fields
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)

    class Meta:
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("organization_Volunteer_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_Volunteer_update", args=(self.pk,))



class Team(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    short_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("organization_Team_detail", args=(self.short_name,))

    def get_update_url(self):
        return reverse("organization_Team_update", args=(self.short_name,))



class TeamMembership(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    member = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    role = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("organization_TeamMembership_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_TeamMembership_update", args=(self.pk,))



class Event(models.Model):

    # Fields
    end_date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("organization_Event_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_Event_update", args=(self.pk,))



class EventMembership(models.Model):

    # Relationships
    event = models.ForeignKey("organization.Event", on_delete=models.CASCADE)
    member = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("organization_EventMembership_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_EventMembership_update", args=(self.pk,))






