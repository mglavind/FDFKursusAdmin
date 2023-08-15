from django import forms
from Depot.models import DepotBox
from organization.models import Team
from Depot.models import DepotItem
from organization.models import Volunteer
from Depot.models import DepotLocation
from . import models


class DepotItemForm(forms.ModelForm):
    class Meta:
        model = models.DepotItem
        fields = [
            "description",
            "name",
            "box",
        ]

    def __init__(self, *args, **kwargs):
        super(DepotItemForm, self).__init__(*args, **kwargs)
        self.fields["box"].queryset = DepotBox.objects.all()



class DepotLocationForm(forms.ModelForm):
    class Meta:
        model = models.DepotLocation
        fields = [
            "address",
            "name",
            "description",
        ]


class DepotBookingForm(forms.ModelForm):
    class Meta:
        model = models.DepotBooking
        fields = [
            "remarks",
            "end",
            "start",
            "status",
            "quantity",
            "team",
            "item",
            "team_contact",
        ]

    def __init__(self, *args, **kwargs):
        super(DepotBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = DepotItem.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()



class DepotBoxForm(forms.ModelForm):
    class Meta:
        model = models.DepotBox
        fields = [
            "name",
            "description",
            "location",
        ]

    def __init__(self, *args, **kwargs):
        super(DepotBoxForm, self).__init__(*args, **kwargs)
        self.fields["location"].queryset = DepotLocation.objects.all()

