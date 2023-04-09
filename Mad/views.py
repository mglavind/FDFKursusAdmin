from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class MadItemListView(generic.ListView):
    model = models.MadItem
    form_class = forms.MadItemForm


class MadItemCreateView(generic.CreateView):
    model = models.MadItem
    form_class = forms.MadItemForm


class MadItemDetailView(generic.DetailView):
    model = models.MadItem
    form_class = forms.MadItemForm


class MadItemUpdateView(generic.UpdateView):
    model = models.MadItem
    form_class = forms.MadItemForm
    pk_url_kwarg = "pk"


class MadItemDeleteView(generic.DeleteView):
    model = models.MadItem
    success_url = reverse_lazy("Mad_MadItem_list")


class MadKategoriListView(generic.ListView):
    model = models.MadKategori
    form_class = forms.MadKategoriForm


class MadKategoriCreateView(generic.CreateView):
    model = models.MadKategori
    form_class = forms.MadKategoriForm


class MadKategoriDetailView(generic.DetailView):
    model = models.MadKategori
    form_class = forms.MadKategoriForm


class MadKategoriUpdateView(generic.UpdateView):
    model = models.MadKategori
    form_class = forms.MadKategoriForm
    pk_url_kwarg = "pk"


class MadKategoriDeleteView(generic.DeleteView):
    model = models.MadKategori
    success_url = reverse_lazy("Mad_MadKategori_list")


class MadBookingListView(generic.ListView):
    model = models.MadBooking
    form_class = forms.MadBookingForm


class MadBookingCreateView(generic.CreateView):
    model = models.MadBooking
    form_class = forms.MadBookingForm


class MadBookingDetailView(generic.DetailView):
    model = models.MadBooking
    form_class = forms.MadBookingForm


class MadBookingUpdateView(generic.UpdateView):
    model = models.MadBooking
    form_class = forms.MadBookingForm
    pk_url_kwarg = "pk"


class MadBookingDeleteView(generic.DeleteView):
    model = models.MadBooking
    success_url = reverse_lazy("Mad_MadBooking_list")
