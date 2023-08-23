from django import forms
from django.forms.widgets import SelectDateWidget
from organization.models import Team, TeamMembership, Volunteer
from Teknik.models import TeknikItem, TeknikType, TeknikBooking
from django.contrib.auth.models import Group
from . import models

class TeknikBookingForm(forms.ModelForm):
    class Meta:
        model = models.TeknikBooking
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
        super(TeknikBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = TeknikItem.objects.all()
        
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
