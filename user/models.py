from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEAMLEDER = "TEAMLEDER", "Teamleder"
        MEDARBEJDER = "MEDARBEJDER", "Medarbejder"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class MedarbejderManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MEDARBEJDER)


class Medarbejder(User):

    base_role = User.Role.MEDARBEJDER

    student = MedarbejderManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Kun for medarbejdere"


@receiver(post_save, sender=Medarbejder)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "MEDARBEJDER":
        MedarbejderProfile.objects.create(user=instance)


class MedarbejderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medarbejder_id = models.IntegerField(null=True, blank=True)


class TeamlederManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEAMLEDER)


class Teamleder(User):

    base_role = User.Role.TEAMLEDER

    teacher = TeamlederManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Kun for Teamledere"


class TeamlederProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teamleder_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Teamleder)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "TEAMLEDER":
        TeamlederProfile.objects.create(user=instance)
