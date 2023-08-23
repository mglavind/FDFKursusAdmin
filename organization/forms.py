from django import forms
from organization.models import Team
from organization.models import Event
from .models import Volunteer
from . import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Volunteer  # Use your custom Volunteer model here
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = [
            "name",
            "short_name",
        ]


class TeamMembershipForm(forms.ModelForm):
    class Meta:
        model = models.TeamMembership
        fields = [
            "member",
            "team",
            "role",
        ]

    def __init__(self, *args, **kwargs):
        super(TeamMembershipForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["member"].queryset = Volunteer.objects.all()



class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = [
            "end_date",
            "name",
            "start_date",
        ]


class EventMembershipForm(forms.ModelForm):
    class Meta:
        model = models.EventMembership
        fields = [
            "event",
            "member",
        ]

    def __init__(self, *args, **kwargs):
        super(EventMembershipForm, self).__init__(*args, **kwargs)
        self.fields["event"].queryset = Event.objects.all()
        self.fields["member"].queryset = Volunteer.objects.all()



class VolunteerForm(forms.ModelForm):
    class Meta:
        model = models.Volunteer
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
        ]