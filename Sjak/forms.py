from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer, Event, EventMembership
from Sjak.models import SjakItem, SjakBooking, SjakItemType
from django.contrib.auth.models import Group
from django.forms import BaseFormSet, TextInput, formset_factory
import datetime
from django.utils import timezone

from . import models
from django.contrib.auth import get_user_model

from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import BaseFormSet, TextInput, formset_factory

from django_bootstrap5.widgets import RadioSelectButtonGroup




class SjakBookingForm(forms.Form): 
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
    team_contact = forms.ChoiceField(
        choices=[(user.id, f"{user.first_name} {user.last_name}") for user in get_user_model().objects.all().order_by("first_name")]
    )
    item = forms.ChoiceField(choices=[(item.id, item.name) for item in SjakItem.objects.all().order_by("name")])
    team = forms.ChoiceField(
        choices=[(team.id, team.name) for team in Team.objects.all().order_by("name")]
    )
    remarks = forms.CharField(widget=forms.Textarea, required=False)
    quantity = forms.DecimalField(max_digits=10, decimal_places=1, required=True)

    class Meta:
       model = SjakBooking
       fields = [
            "start",
            "end",
            "team_contact",
            "item",
            "team",
            "remarks",
            "quantity",
       ] # list of fields you want from model

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
        

   

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        instance.status_internal = "Afventer"
        instance.event = Event.objects.filter(is_active=True).first().id
        deadline = Event.objects.filter(is_active=True).first().deadline_sjak
        if deadline < timezone.now().date():
            if commit:
                instance.save()
        return instance

    


            
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


