from django import forms
from Depot.models import DepotBox
from organization.models import Team
from Depot.models import DepotItem
from organization.models import Volunteer
from Depot.models import DepotLocation
from organization.models import Team, TeamMembership
from django.core.validators import MaxValueValidator
from django.utils import timezone
from . import models


class DepotItemForm(forms.ModelForm):
    class Meta:
        model = models.DepotItem
        fields = [
            "name",
            "description",
            "unit",
            "quantity_lager",
            "box",
        ]

    def __init__(self, *args, **kwargs):
        super(DepotItemForm, self).__init__(*args, **kwargs)
        self.fields["box"].queryset = DepotBox.objects.all()



class DepotLocationForm(forms.ModelForm):
    class Meta:
        model = models.DepotLocation
        fields = [
            "address",
            "name",
            "description",
        ]


class DepotBookingForm(forms.ModelForm):
    class Meta:
        model = models.DepotBooking
        exclude = ['status']
        fields = [
            "remarks",
            "end",
            "start",
            "quantity",
            "team",
            "item",
            "team_contact",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(DepotBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = DepotItem.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()
        self.fields["team"].queryset = Team.objects.all()
        
        if user:
            try:
                team_membership = TeamMembership.objects.get(member=user)
                self.fields["team"].initial = team_membership.team
                self.fields["team_contact"].queryset = Volunteer.objects.filter(
                    teammembership__team=team_membership.team
                )
            except TeamMembership.DoesNotExist:
                pass

            self.fields["team_contact"].initial = user

    


class DepotBoxForm(forms.ModelForm):
    class Meta:
        model = models.DepotBox
        fields = [
            "name",
            "description",
            "location",
        ]

    def __init__(self, *args, **kwargs):
        super(DepotBoxForm, self).__init__(*args, **kwargs)
        self.fields["location"].queryset = DepotLocation.objects.all()

