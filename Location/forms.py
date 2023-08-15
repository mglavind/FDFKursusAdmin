from django import forms
from organization.models import Volunteer
from Location.models import LocationItem
from organization.models import Team
from Location.models import LocationType
from . import models


class LocationTypeForm(forms.ModelForm):
    class Meta:
        model = models.LocationType
        fields = [
            "description",
            "name",
        ]


class LocationBookingForm(forms.ModelForm):
    class Meta:
        model = models.LocationBooking
        fields = [
            "end",
            "status",
            "remarks",
            "start",
            "primary_camp",
            "team_contact",
            "item",
            "team",
        ]

    def __init__(self, *args, **kwargs):
        super(LocationBookingForm, self).__init__(*args, **kwargs)
        self.fields["team_contact"].queryset = Volunteer.objects.all()
        self.fields["item"].queryset = LocationItem.objects.all()
        self.fields["team"].queryset = Team.objects.all()



class LocationItemForm(forms.ModelForm):
    class Meta:
        model = models.LocationItem
        fields = [
            "name",
            "description",
            "type",
        ]

    def __init__(self, *args, **kwargs):
        super(LocationItemForm, self).__init__(*args, **kwargs)
        self.fields["type"].queryset = LocationType.objects.all()

