from django import forms
from django.core.validators import MaxValueValidator
from django.utils import timezone
from organization.models import Team, TeamMembership
from AktivitetsTeam.models import AktivitetsTeamItem
from organization.models import Volunteer
from . import models

from organization.models import Team


class AktivitetsTeamItemForm(forms.ModelForm):
    class Meta:
        model = models.AktivitetsTeamItem
        fields = [
            "description",
            "name",
        ]


class AktivitetsTeamBookingForm(forms.ModelForm):
    start_date = forms.DateField(
        label="Start Date",
        initial=timezone.now().date(),
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    start_time = forms.TimeField(
        label="Start Time",
        initial=timezone.now().time(),
        widget=forms.TimeInput(attrs={"type": "time"}),
    )
    

    my_specific_team = Team.objects.get(id=8)
    assigned_aktivitetsteam = forms.ModelMultipleChoiceField(
        queryset=Volunteer.objects.filter(teammembership__team=my_specific_team),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = models.AktivitetsTeamBooking
        fields = '__all__' 
 


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

            instance = kwargs.get('instance')
            if instance:
                self.fields["start_date"] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
                self.fields["start_time"] = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
                self.fields["end_date"] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
                self.fields["end_time"] = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

        else:
            self.fields["start_date"] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
            self.fields["start_time"] = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
            self.fields["end_date"] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
            self.fields["end_time"] = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

        if instance:
            self.fields["remarks"].initial = instance.remarks
            self.fields["location"].initial = instance.location

