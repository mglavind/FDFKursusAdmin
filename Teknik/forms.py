from django import forms
from organization.models import Team
from Teknik.models import TeknikItem
from organization.models import Volunteer
from django.contrib.auth.models import Group
from Teknik.models import TeknikType
from . import models


class TeknikBookingForm(forms.ModelForm):
    class Meta:
        model = models.TeknikBooking
        fields = [
            "quantity",
            "end",
            "start",
            "status",
            "team",
            "item",
            "team_contact",
        ]

    def __init__(self, *args, **kwargs):
        super(TeknikBookingForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.all()
        self.fields["item"].queryset = TeknikItem.objects.all()
        self.fields["team_contact"].queryset = Volunteer.objects.all()



class TeknikItemForm(forms.ModelForm):
    class Meta:
        model = models.TeknikItem
        fields = [
            "name",
            "image",
            "description",
            "owner",
            "type",
        ]

    def __init__(self, *args, **kwargs):
        super(TeknikItemForm, self).__init__(*args, **kwargs)
        self.fields["owner"].queryset = Group.objects.all()
        self.fields["type"].queryset = TeknikType.objects.all()



class TeknikTypeForm(forms.ModelForm):
    class Meta:
        model = models.TeknikType
        fields = [
            "name",
        ]
