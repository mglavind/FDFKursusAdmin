from django import forms
from organization.models import Team
from Location.models import LocationItem
from organization.models import Volunteer
from organization.models import Team, TeamMembership, Event
from django.core.validators import MaxValueValidator
from django.utils import timezone
from . import models
from django.forms import BaseFormSet, TextInput, formset_factory

class LocationTypeForm(forms.ModelForm):
    class Meta:
        model = models.LocationType
        fields = [
            "description",
            "name",
        ]


class LocationBookingForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=TextInput(attrs={"type": "date"}),
        initial=Event.objects.filter(is_active=True).first().start_date
    )
    start_time = forms.TimeField(
        widget=TextInput(attrs={"type": "time"}),
        initial=Event.objects.filter(is_active=True).first().start_date
    )
    end_date = forms.DateField(
        widget=TextInput(attrs={"type": "date"}),
        initial=Event.objects.filter(is_active=True).first().end_date,
    )
    end_time = forms.TimeField(
        widget=TextInput(attrs={"type": "time"}),
        initial=Event.objects.filter(is_active=True).first().end_date
    )
    class Meta:
        model = models.LocationBooking
        fields = [
            "remarks",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
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
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = LocationItem.objects.all()
        
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
            
            # Set initial values from instance
            instance = kwargs.get('instance')
            if instance:
                self.fields["quantity"].initial = instance.quantity
                self.fields["start_date"].initial = instance.start_date
                self.fields["end_date"].initial = instance.end_date
                self.fields["start_time"].initial = instance.start_time
                self.fields["end_time"].initial = instance.end_time
                # Add other fields similarly



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

