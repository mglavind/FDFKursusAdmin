from django import forms
from organization.models import Team
from Foto.models import FotoItem
from organization.models import Team, TeamMembership, Volunteer
from . import models


class FotoItemForm(forms.ModelForm):
    class Meta:
        model = models.FotoItem
        fields = [
            "name",
            "description",
        ]



class FotoBookingForm(forms.ModelForm):
    class Meta:
        model = models.FotoBooking
        fields = [
            "start",
            "end",
            "remarks",
            "location",
            "status",
            "team",
            "item",
            "team_contact",
        ]

    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(FotoBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = FotoItem.objects.all()
        
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

