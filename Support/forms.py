from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer
from Support.models import SupportItem, SupportItemType, SupportBooking
from django.contrib.auth.models import Group
from . import models


class SupportBookingForm(forms.ModelForm):
    class Meta:
        model = models.SupportBooking
        fields = [
            "item",
            "team_contact",
            "team",
            "remarks",
            "start",
            "end",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(SupportBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = SupportItem.objects.all().order_by("name")
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
                self.fields["start"].initial = instance.start
                self.fields["end"].initial = instance.start

                # Add other fields similarly

            
class SupportItemForm(forms.ModelForm):
    class Meta:
        model = models.SupportItem
        fields = [
            "name",
            "description",
            "type",
        ]

    def __init__(self, *args, **kwargs):
        super(SupportItemForm, self).__init__(*args, **kwargs)
        self.fields["type"].queryset = SupportItemType.objects.all().order_by("name")






class SupportItemTypeForm(forms.ModelForm):
    class Meta:
        model = models.SupportItemType
        fields = [
            "name",
            "description",
        ]
