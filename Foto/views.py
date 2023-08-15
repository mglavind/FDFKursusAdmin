from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class FotoItemListView(generic.ListView):
    model = models.FotoItem
    form_class = forms.FotoItemForm


class FotoItemCreateView(generic.CreateView):
    model = models.FotoItem
    form_class = forms.FotoItemForm


class FotoItemDetailView(generic.DetailView):
    model = models.FotoItem
    form_class = forms.FotoItemForm


class FotoItemUpdateView(generic.UpdateView):
    model = models.FotoItem
    form_class = forms.FotoItemForm
    pk_url_kwarg = "pk"


class FotoItemDeleteView(generic.DeleteView):
    model = models.FotoItem
    success_url = reverse_lazy("Foto_FotoItem_list")


class FotoBookingListView(generic.ListView):
    model = models.FotoBooking
    form_class = forms.FotoBookingForm


class FotoBookingCreateView(generic.CreateView):
    model = models.FotoBooking
    form_class = forms.FotoBookingForm


class FotoBookingDetailView(generic.DetailView):
    model = models.FotoBooking
    form_class = forms.FotoBookingForm


class FotoBookingUpdateView(generic.UpdateView):
    model = models.FotoBooking
    form_class = forms.FotoBookingForm
    pk_url_kwarg = "pk"


class FotoBookingDeleteView(generic.DeleteView):
    model = models.FotoBooking
    success_url = reverse_lazy("Foto_FotoBooking_list")
