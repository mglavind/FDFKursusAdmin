from django import forms
from Depot.models import DepotBox, DepotBooking
from organization.models import Team
from Depot.models import DepotItem
from organization.models import Team, TeamMembership, Volunteer, Event, EventMembership
from Depot.models import DepotLocation
from django.core.validators import MaxValueValidator
from django.utils import timezone
from . import models

from django.forms import BaseFormSet, TextInput, formset_factory


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
    start = forms.DateField(
        widget=TextInput(attrs={"type": "date"}),
        initial=Event.objects.filter(is_active=True).first().start_date
    )
    start_time = forms.TimeField(
        widget=TextInput(attrs={"type": "time"}),
        initial=Event.objects.filter(is_active=True).first().start_date
    )
    end = forms.DateField(
        widget=TextInput(attrs={"type": "date"}),
        initial=Event.objects.filter(is_active=True).first().end_date,
    )
    end_time = forms.TimeField(
        widget=TextInput(attrs={"type": "time"}),
        initial=Event.objects.filter(is_active=True).first().end_date
    )
    class Meta:
        model = models.DepotBooking
        exclude = ['status']
        fields = [
            "start",
            "start_time",
            "end",
            "end_time",
            "remarks",
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
        self.fields["item"].queryset = DepotItem.objects.all().order_by("name")
        self.fields["team_contact"].queryset = Volunteer.objects.all().order_by("first_name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")
        
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

