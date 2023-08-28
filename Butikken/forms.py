from django import forms
from Butikken.models import ButikkenItemType, ButikkenItem
from organization.models import Team, TeamMembership, Volunteer
from . import models


class ButikkenItemForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenItem
        fields = [
            "description",
            "name",
            "type",
            "content_normal",
            "content_unit",
        ]

    def __init__(self, *args, **kwargs):
        super(ButikkenItemForm, self).__init__(*args, **kwargs)
        self.fields["type"].queryset = ButikkenItemType.objects.all()



class ButikkenBookingForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenBooking
        fields = [
            "remarks",
            "quantity",
            "start",
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
        super(ButikkenBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = ButikkenItem.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()
        self.fields["team"].queryset = Team.objects.all()
        
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



class ButikkenItemTypeForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenItemType
        fields = [
            "name",
            "description",
        ]
