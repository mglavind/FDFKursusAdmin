from django import forms
from Mad.models import MadKategori
from . import models


class MadItemForm(forms.ModelForm):
    class Meta:
        model = models.MadItem
        fields = [
            "indhold",
            "er_aktiv",
            "enhed",
            "kategori",
        ]

    def __init__(self, *args, **kwargs):
        super(MadItemForm, self).__init__(*args, **kwargs)
        self.fields["kategori"].queryset = MadKategori.objects.all()



class MadKategoriForm(forms.ModelForm):
    class Meta:
        model = models.MadKategori
        fields = [
            "navn",
        ]


class MadBookingForm(forms.ModelForm):
    class Meta:
        model = models.MadBooking
        fields = [
            "aktivitet",
            "forklaring",
            "antal",
            "status",
            "anvendelses_tidspunkt",
        ]
