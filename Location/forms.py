from django import forms
from organization.models import Team
from Location.models import LocationItem
from organization.models import Volunteer
from organization.models import Team, TeamMembership
from django.core.validators import MaxValueValidator
from django.utils import timezone
from . import models

class LocationTypeForm(forms.ModelForm):
    class Meta:
        model = models.LocationType
        fields = [
            "description",
            "name",
        ]


class LocationBookingForm(forms.ModelForm):
    class Meta:
        model = models.LocationBooking
        fields = [
            "end",
            "remarks",
            "start",
            "primary_camp",
            "team_contact",
            "item",
            "team",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(LocationBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = LocationItem.objects.all().order_by("name")
        self.fields["team_contact"].queryset = Volunteer.objects.all().order_by("first_name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")
        print(user) 
        if user:
            try:
                team_membership = TeamMembership.objects.get(member=user)
                self.fields["team"].initial = team_membership.team
                self.fields["team_contact"].initial = user
                self.fields["team_contact"].queryset = Volunteer.objects.filter(
                    teammembership__team=team_membership.team
                )
            except TeamMembership.DoesNotExist:
                pass



class LocationItemForm(forms.ModelForm):
    class Meta:
        model = models.LocationItem
        fields = [
            "name",
            "description",
            "type",
        ]

    def __init__(self, *args, **kwargs):
        super(LocationItemForm, self).__init__(*args, **kwargs)
        self.fields["type"].queryset = LocationType.objects.all()

