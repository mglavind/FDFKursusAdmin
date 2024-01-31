from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer, Event
from SOS.models import SOSItem, SOSType, SOSBooking
from django.contrib.auth.models import Group
from . import models
from django.forms import BaseFormSet, TextInput, formset_factory


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



    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(SOSBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = SOSItem.objects.all()
        
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
