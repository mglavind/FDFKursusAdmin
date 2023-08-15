from django import forms
from organization.models import Team
from Foto.models import FotoItem
from organization.models import Volunteer
from . import models


class FotoItemForm(forms.ModelForm):
    class Meta:
        model = models.FotoItem
        fields = []



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

    def __init__(self, *args, **kwargs):
        super(FotoBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = FotoItem.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()

