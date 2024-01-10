from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.urls import reverse








class Event(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    deadline_sjak = models.DateField()
    deadline_teknik = models.DateField()
    deadline_mad = models.DateField()
    deadline_aktivitetsteam = models.DateField()
    deadline_foto = models.DateField()
    deadline_lokaler = models.DateField()
    deadline_sos = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("organization_Event_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_Event_update", args=(self.pk,))




    
class Volunteer(AbstractUser):

    # Fields
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)
    events = models.ManyToManyField(Event, through='EventMembership')

    class Meta:
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("organization_Volunteer_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_Volunteer_update", args=(self.pk,))
    

class Todo(models.Model):
    description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class EventMembership(models.Model):

    # Relationships
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

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
    



class Team(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=30)   
    events = models.ManyToManyField(Event, through='TeamEventMembership') 
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)



    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("organization_Team_detail", args=(self.short_name,))

    def get_update_url(self):
        return reverse("organization_Team_update", args=(self.short_name,))


class TeamEventMembership(models.Model):

    # Relationships
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("organization_TeamEventMembership_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_TeamEventMembership_update", args=(self.pk,))


class TeamMembership(models.Model):

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    member = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    role = models.CharField(max_length=30, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("organization_TeamMembership_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_TeamMembership_update", args=(self.pk,))




class Key(models.Model):

    # Relationships
    current_user = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE, blank=True, null=True)

    # Fields
    description = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("organization_Key_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_Key_update", args=(self.pk,))






