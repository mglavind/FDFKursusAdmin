from django import forms
from django.core.validators import MaxValueValidator
from django.utils import timezone
from organization.models import Team, TeamMembership, Volunteer, Event, EventMembership
from AktivitetsTeam.models import AktivitetsTeamItem
from organization.models import Volunteer
from . import models
from django.forms import BaseFormSet, TextInput, formset_factory
from organization.models import Team
from django.utils import timezone
from datetime import time

class AktivitetsTeamItemForm(forms.ModelForm):
    class Meta:
        model = models.AktivitetsTeamItem
        fields = [
            "name",
            "description",
            "youtube_link",
            "short_description",
        ]


class AktivitetsTeamBookingForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=TextInput(attrs={"type": "date"}),
        initial=Event.objects.filter(is_active=True).first().start_date,
        label="Start Dato:"
    )
    start_time = forms.TimeField(
        widget=TextInput(attrs={"type": "time"}),
        initial=Event.objects.filter(is_active=True).first().start_date,
        label="Start tidspunk:"
    )
    end_date = forms.DateField(
        widget=TextInput(attrs={"type": "date"}),
        initial=Event.objects.filter(is_active=True).first().end_date,
        label="Slut dato:"
    )
    end_time = forms.TimeField(
        widget=TextInput(attrs={"type": "time"}),
        initial=Event.objects.filter(is_active=True).first().end_date,
        label="Slut tidspunkt:"
    )
    my_specific_team = Team.objects.get(id=8)
    assigned_aktivitetsteam = forms.ModelMultipleChoiceField(
        queryset=Volunteer.objects.filter(teammembership__team=my_specific_team),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = models.AktivitetsTeamBooking
        fields = [
            "item",
            "team",
            "team_contact",
            "remarks",
            "location",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "latitude",
            "longitude",
            "address",
        ]
        widgets = {
            "item": forms.Select(attrs={"class": "form-select"}),
            "team": forms.Select(attrs={"class": "form-select"}),
            "team_contact": forms.Select(attrs={"class": "form-select"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "remarks": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": (
                    "Hvad er jeres formål med denne aktivitet? Er der en temaramme det passer ind i? Skal vi spille en rolle? "
                    "Hvor mange deltagere? Kommer I på én gang eller i mindre hold? Hvor store hold? "
                    "Hvis der skal bruges materialer, giver I os dem? Eller forventer I at vi finder hvad der skal bruges? "
                    "Falder jeres program uden denne aktivitet, eller er det noget vi kan finde et alternativ til, eller et andet tidspunkt til, hvis nødvendigt? "
                    "Har I snakket med en fra Support om denne booking? Hvem, og giv gerne et recap. De husker ikke så godt 🙂 "
                    "Vil der være en instruktør til stede? "
                    "Er der andet vi skal være opmærksomme på?"
                )
            }),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "latitude": forms.TextInput(attrs={"class": "form-control"}),
            "longitude": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),            
        }
        labels = {
            "item": "Aktivitet",
            "team": "Team",
            "team_contact": "Kontaktperson",
            "quantity": "Antal",
            "remarks": "Bemærkninger",
            "location": "Lokation",
            "latitude" : "latitude",
            "longitude": "longitude",
            "address": "Addresse",
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance
    
    def __init__(self, *args, user=None, **kwargs):
        super(AktivitetsTeamBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = AktivitetsTeamItem.objects.all().order_by("name")
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

# Function to get the next event
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
            self.fields["location"].initial = instance.location
        else:
            # Use the next event's start date if no instance or new instance
            next_event = get_next_event()
            if next_event:
                self.fields["start_date"].initial = next_event.start_date.strftime('%Y-%m-%d')
                self.fields["start_time"].initial = time(8, 0)  # Set default time to 08:00 AM
                self.fields["end_time"].initial = time(8, 0)  # Set default time to 08:00 AM
                self.fields["end_date"].initial = next_event.end_date.strftime('%Y-%m-%d')
