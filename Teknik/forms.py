from django import forms
from organization.models import Team, TeamMembership, Volunteer
from Teknik.models import TeknikItem, TeknikType, TeknikBooking
from django.contrib.auth.models import Group
from . import models


class TeknikBookingForm(forms.ModelForm):
    class Meta:
        model = models.TeknikBooking
        fields = [
            "quantity",
            "status",
            "team",
            "item",
            "start",
            "end",
            "team_contact",
            "remarks",
        ]

    widgets = {
        "status": forms.TextInput(attrs={"value": "Pending", "disabled": True}),
    }

    status = forms.ChoiceField(choices=models.TeknikBooking.STATUS_CHOICES, widget=forms.HiddenInput, initial='Pending')

    def __init__(self, *args, user=None, **kwargs):
        super(TeknikBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = TeknikItem.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()
        self.fields["status"].initial = "Pending"
        self.fields["status"].widget.attrs["readonly"] = True
        
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
            self.fields["status"].initial = "Pending"



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
