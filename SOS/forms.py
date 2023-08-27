from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer
from SOS.models import SOSItem, SOSType, SOSBooking
from django.contrib.auth.models import Group
from . import models

class SOSBookingForm(forms.ModelForm):
    class Meta:
        model = models.SOSBooking
        fields = [
            "quantity",
            "team",
            "item",
            "start",
            "end",
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
                self.fields["start"].initial = instance.start
                self.fields["end"].initial = instance.end
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
