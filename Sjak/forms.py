from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer
from Sjak.models import SjakItem, SjakBooking
from django.contrib.auth.models import Group
from . import models


class SjakBookingForm(forms.ModelForm):
    class Meta:
        model = models.SjakBooking
        fields = [
            "remarks",
            "quantity",
            "start",
            "end",
            "item",
            "team_contact",
            "team",
        ]

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
                self.fields["start"].initial = instance.start

                # Add other fields similarly

            
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
