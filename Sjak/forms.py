from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer, Event, EventMembership
from Sjak.models import SjakItem, SjakBooking, SjakItemType
from django.contrib.auth.models import Group
from django.forms import BaseFormSet, TextInput, formset_factory
import datetime
from datetime import time
from django.utils import timezone

from . import models
from django.contrib.auth import get_user_model

from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import BaseFormSet, TextInput, formset_factory

from django_bootstrap5.widgets import RadioSelectButtonGroup




class SjakBookingForm(forms.ModelForm): 
    # To update the form, you need to update the model and the form
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
    remarks = forms.CharField(widget=forms.Textarea, required=False)
    quantity = forms.DecimalField(max_digits=10, decimal_places=1, required=True)

    class Meta:
        model = models.SjakBooking
        fields = [
                "start",
                "start_time",
                "end",
                "end_time",
                "team_contact",
                "item",
                "team",
                "remarks",
                "quantity",
        ] # list of fields you want from model
        widgets = {
            "item": forms.Select(attrs={"class": "form-select"}),
            "team": forms.Select(attrs={"class": "form-select"}),
            "team_contact": forms.Select(attrs={"class": "form-select"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "start": forms.DateInput(attrs={"class": "form-control"}),
            "start_time": forms.TimeInput(attrs={"class": "form-control"}),
            "end": forms.DateInput(attrs={"class": "form-control"}),
            "end_time": forms.TimeInput(attrs={"class": "form-control"}),
            "remarks": forms.Textarea(attrs={"class": "form-control"}),
        }
        labels = {
            "quantity": "Antal",
            "team": "Team",
            "item": "Sjak ting",
            "start": "Start Dato",
            "start_time": "Start tidspunkt",
        }

    def save(self, commit=True):
        print("Begin save")
        instance = super().save(commit=False)
        instance.status = "Pending"
        instance.status_internal = "Afventer"
        if commit:
            print("Connet exists")
            instance.save()
            print("instance saved")
        return instance


    def __init__(self, *args, user=None, **kwargs):
        super(SjakBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = SjakItem.objects.all().order_by("name")
        self.fields["team_contact"].queryset = Volunteer.objects.all().order_by("first_name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")
        print("user", user)
        self.fields["team_contact"].initial = user
        if user:
            print("A user exists")
            team_membership = TeamMembership.objects.get(member=user)
            self.fields["team"].initial = team_membership.team
            self.fields["team_contact"].queryset = Volunteer.objects.filter(
                teammembership__team=team_membership.team
            )
            self.fields["team_contact"].initial = user
# Function to get the next event
        def get_next_event():
            now = timezone.now()
            next_event = Event.objects.filter(start_date__gt=now).order_by('start_date').first()
            return next_event
        
        # Set initial values from instance
        instance = kwargs.get('instance')
        if instance:
            self.fields["quantity"].initial = instance.quantity
            self.fields["start"].initial = instance.start
            self.fields["end"].initial = instance.end
            self.fields["start_time"].initial = instance.start_time
            self.fields["end_time"].initial = instance.end_time
        else:
            # Use the next event's start date if no instance or new instance
            next_event = get_next_event()
            if next_event:
                self.fields["start"].initial = next_event.start_date.strftime('%Y-%m-%d')
                self.fields["start_time"].initial = time(8, 0)  # Set default time to 08:00 AM
                self.fields["end_time"].initial = time(8, 0)  # Set default time to 08:00 AM
                self.fields["end"].initial = next_event.end_date.strftime('%Y-%m-%d')

            
class SjakItemForm(forms.ModelForm):
    class Meta:
        model = models.SjakItem
        fields = [
            "name",
            "description",
            "item_type",
        ]

    def __init__(self, *args, **kwargs):
        super(SjakItemForm, self).__init__(*args, **kwargs)
        self.fields["item_type"].queryset = SjakItemType.objects.all()






class SjakItemTypeForm(forms.ModelForm):
    class Meta:
        model = models.SjakItemType
        fields = [
            "name",
        ]


