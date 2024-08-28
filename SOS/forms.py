from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer, Event
from SOS.models import SOSItem, SOSType, SOSBooking
from django.contrib.auth.models import Group
from . import models
from django.forms import BaseFormSet, TextInput, formset_factory
from django.utils import timezone
from datetime import time

class SOSBookingForm(forms.ModelForm):
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
        model = models.SOSBooking
        fields = [
            "quantity",
            "team",
            "item",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "team_contact",
            "remarks",
            "delivery_needed",
            "assistance_needed",
        ]
        widgets = {
            "item": forms.Select(attrs={"class": "form-select"}),
            "team": forms.Select(attrs={"class": "form-select"}),
            "team_contact": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "delivery_needed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "assistance_needed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "start_date": forms.DateInput(attrs={"class": "form-control"}),
            "start_time": forms.TimeInput(attrs={"class": "form-control"}),
            "end_date": forms.DateInput(attrs={"class": "form-control"}),
            "end_time": forms.TimeInput(attrs={"class": "form-control"}),  
        }
        labels = {
            "quantity": "Antal",
            "team": "Team",
            "item": "SOS ting",
            "start_date": "Start Dato",
            "start_time": "Start tidspunkt",
            "end_date": "Slut dato",
            "end_time": "Slut tidspunkt",
            "team_contact": "Kontaktperson",
            "remarks": "Bemærkninger",
            "delivery_needed": "Levering nødvendig",
            "assistance_needed": "Vi ønsker assistance",
        }





    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(SOSBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = SOSItem.objects.all()
        self.fields["team"].queryset = Team.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()
        if user:
            print("A user exists")
            team_membership = TeamMembership.objects.get(member=user)
            self.fields["team"].initial = team_membership.team
            self.fields["team_contact"].queryset = Volunteer.objects.filter(
                teammembership__team=team_membership.team
            )
            self.fields["team_contact"].initial = user
        
        def get_next_event():
            now = timezone.now()
            next_event = Event.objects.filter(start_date__gt=now).order_by('start_date').first()
            return next_event
        
        # Set initial values from instance
        instance = kwargs.get('instance')
        if instance:
            self.fields["start_date"].initial = instance.start_date
            self.fields["end_date"].initial = instance.end_date
            self.fields["start_time"].initial = instance.start_time
            self.fields["end_time"].initial = instance.end_time            
            self.fields["remarks"].initial = instance.remarks
        else:
            # Use the next event's start date if no instance or new instance
            next_event = get_next_event()
            if next_event:
                self.fields["start_date"].initial = next_event.start_date.strftime('%Y-%m-%d')
                self.fields["start_time"].initial = time(8, 0)  # Set default time to 08:00 AM
                self.fields["end_time"].initial = time(8, 0)  # Set default time to 08:00 AM
                self.fields["end_date"].initial = next_event.end_date.strftime('%Y-%m-%d')


class SOSItemForm(forms.ModelForm):
    class Meta:
        model = models.SOSItem
        fields = [
            "name",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super(SOSItemForm, self).__init__(*args, **kwargs)



class SOSTypeForm(forms.ModelForm):
    class Meta:
        model = models.SOSType
        fields = [
            "name",
        ]
