from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Volunteer(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
    

class Team(models.Model):
    name = models.CharField(max_length=255)
    team_number = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class TeamMembership(models.Model):
    user = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.team.name}"


class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    

class EventMembership(models.Model):
    user = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"