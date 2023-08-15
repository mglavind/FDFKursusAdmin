from django import forms
from Butikken.models import ButikkenItemType
from organization.models import Team
from Butikken.models import ButikkenItem
from organization.models import Volunteer
from . import models


class ButikkenItemForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenItem
        fields = [
            "description",
            "name",
            "type",
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
            "status",
            "start",
            "team",
            "item",
            "team_contact",
        ]

    def __init__(self, *args, **kwargs):
        super(ButikkenBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = ButikkenItem.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()



class ButikkenItemTypeForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenItemType
        fields = [
            "name",
            "description",
        ]
