from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer, Event
from Teknik.models import TeknikItem, TeknikType, TeknikBooking
from django.contrib.auth.models import Group
from . import models
from django.forms import BaseFormSet, TextInput, formset_factory

class TeknikBookingForm(forms.ModelForm):
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
        model = models.TeknikBooking
        
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
        print("TeknikBookingForm.save() begin")
        instance = super().save(commit=False)
        print("instance loaded")
        instance.status = "Pending"
        print("Instance set to pending")
        if commit:
            print("Connet exists")
            instance.save()
            print("instance saved")
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(TeknikBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all().order_by("name")
        self.fields["item"].queryset = TeknikItem.objects.all().order_by("name")
        
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
                # Add other fields similarly



class TeknikItemForm(forms.ModelForm):
    class Meta:
        model = models.TeknikItem
        fields = [
            "name",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super(TeknikItemForm, self).__init__(*args, **kwargs)



class TeknikTypeForm(forms.ModelForm):
    class Meta:
        model = models.TeknikType
        fields = [
            "name",
        ]
