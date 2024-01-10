from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer, Event, EventMembership
from Sjak.models import SjakItem, SjakBooking
from django.contrib.auth.models import Group
import datetime
from django.utils import timezone

from . import models
from django.contrib.auth import get_user_model


class SjakBookingForm(forms.ModelForm):

    class Meta:
        model = models.SjakBooking
        fields = '__all__' 

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(SjakBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = SjakItem.objects.all().order_by("name")
        self.fields["team_contact"].queryset = Volunteer.objects.all().order_by("first_name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")
        self.fields["team_contact"].initial = user

        # Set team_contact to current user if the form is being created
        if not self.instance.pk:
            self.fields["team_contact"].initial = user
        else:
            # For update, disable team_contact field to prevent changes
            self.fields["team_contact"].widget.attrs["readonly"] = True
            self.fields["team_contact"].widget.attrs["disabled"] = True



        
        
    

            
class SjakItemForm(forms.ModelForm):
    class Meta:
        model = models.SjakItem
        fields = [
            "name",
            "description",
            "type",
        ]

    def __init__(self, *args, **kwargs):
        super(SjakItemForm, self).__init__(*args, **kwargs)
        self.fields["type"].queryset = SjakItemType.objects.all()






class SjakItemTypeForm(forms.ModelForm):
    class Meta:
        model = models.SjakItemType
        fields = [
            "name",
        ]
