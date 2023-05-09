from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

class MedarbejderListView(generic.ListView):
    model = models.Medarbejder
    form_class = forms.MedarbejderForm


class MedarbejderCreateView(generic.CreateView):
    model = models.Medarbejder
    form_class = forms.MedarbejderForm


class MedarbejderDetailView(generic.DetailView):
    model = models.Medarbejder
    form_class = forms.MedarbejderForm


class MedarbejderUpdateView(generic.UpdateView):
    model = models.Medarbejder
    form_class = forms.MedarbejderForm
    pk_url_kwarg = "pk"


class MedarbejderDeleteView(generic.DeleteView):
    model = models.Medarbejder
    success_url = reverse_lazy("KursusOrganisation_Medarbejder_list")


class KursusListView(generic.ListView):
    model = models.Kursus
    form_class = forms.KursusForm


class KursusCreateView(generic.CreateView):
    model = models.Kursus
    form_class = forms.KursusForm


class KursusDetailView(generic.DetailView):
    model = models.Kursus
    form_class = forms.KursusForm


class KursusUpdateView(generic.UpdateView):
    model = models.Kursus
    form_class = forms.KursusForm
    pk_url_kwarg = "pk"


class KursusDeleteView(generic.DeleteView):
    model = models.Kursus
    success_url = reverse_lazy("KursusOrganisation_Kursus_list")


class TeamListView(generic.ListView):
    model = models.Team
    form_class = forms.TeamForm


class TeamCreateView(generic.CreateView):
    model = models.Team
    form_class = forms.TeamForm


class TeamDetailView(generic.DetailView):
    model = models.Team
    form_class = forms.TeamForm


class TeamUpdateView(generic.UpdateView):
    model = models.Team
    form_class = forms.TeamForm
    pk_url_kwarg = "pk"


class TeamDeleteView(generic.DeleteView):
    model = models.Team
    success_url = reverse_lazy("KursusOrganisation_Team_list")
