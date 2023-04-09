from django import forms
from django.contrib.auth.models import User
from KursusOrganisation.models import Medarbejder
from KursusOrganisation.models import Kursus
from . import models


class MedarbejderForm(forms.ModelForm):
    class Meta:
        model = models.Medarbejder
        fields = [
            "navn",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(MedarbejderForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()



class KursusForm(forms.ModelForm):
    class Meta:
        model = models.Kursus
        fields = [
            "start_date",
            "navn",
            "end_date",
        ]


class TeamForm(forms.ModelForm):
    medarbejder_p = forms.ModelChoiceField(queryset=None)
    kursus = forms.ModelChoiceField(queryset=None)
    class Meta:
        model = models.Team
        fields = [
            "navn",
            "medarbejder",
            "kursus",
        ]

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields["medarbejder"].queryset = Medarbejder.objects.all()
        self.fields["kursus"].queryset = Kursus.objects.all()

