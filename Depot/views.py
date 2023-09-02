from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from . import models
from . import forms


class DepotItemListView(generic.ListView):
    model = models.DepotItem
    form_class = forms.DepotItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.DepotItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class DepotItemCreateView(generic.CreateView):
    model = models.DepotItem
    form_class = forms.DepotItemForm


class DepotItemDetailView(generic.DetailView):
    model = models.DepotItem
    form_class = forms.DepotItemForm


class DepotItemUpdateView(generic.UpdateView):
    model = models.DepotItem
    form_class = forms.DepotItemForm
    pk_url_kwarg = "pk"


class DepotItemDeleteView(generic.DeleteView):
    model = models.DepotItem
    success_url = reverse_lazy("Depot_DepotItem_list")


class DepotLocationListView(generic.ListView):
    model = models.DepotLocation
    form_class = forms.DepotLocationForm


class DepotLocationCreateView(generic.CreateView):
    model = models.DepotLocation
    form_class = forms.DepotLocationForm


class DepotLocationDetailView(generic.DetailView):
    model = models.DepotLocation
    form_class = forms.DepotLocationForm


class DepotLocationUpdateView(generic.UpdateView):
    model = models.DepotLocation
    form_class = forms.DepotLocationForm
    pk_url_kwarg = "pk"


class DepotLocationDeleteView(generic.DeleteView):
    model = models.DepotLocation
    success_url = reverse_lazy("Depot_DepotLocation_list")


class DepotBookingListView(generic.ListView):
    model = models.DepotBooking
    form_class = forms.DepotBookingForm

    def get_queryset(self):
        return models.DepotBooking.objects.order_by(F('item'),F('start') )


class DepotBookingCreateView(generic.CreateView):
    model = models.DepotBooking
    form_class = forms.DepotBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DepotBookingDetailView(generic.DetailView):
    model = models.DepotBooking
    form_class = forms.DepotBookingForm


class DepotBookingUpdateView(generic.UpdateView):
    model = models.DepotBooking
    form_class = forms.DepotBookingForm
    pk_url_kwarg = "pk"


class DepotBookingDeleteView(generic.DeleteView):
    model = models.DepotBooking
    success_url = reverse_lazy("Depot_DepotBooking_list")


class DepotBoxListView(generic.ListView):
    model = models.DepotBox
    form_class = forms.DepotBoxForm


class DepotBoxCreateView(generic.CreateView):
    model = models.DepotBox
    form_class = forms.DepotBoxForm


class DepotBoxDetailView(generic.DetailView):
    model = models.DepotBox
    form_class = forms.DepotBoxForm


class DepotBoxUpdateView(generic.UpdateView):
    model = models.DepotBox
    form_class = forms.DepotBoxForm
    pk_url_kwarg = "pk"


class DepotBoxDeleteView(generic.DeleteView):
    model = models.DepotBox
    success_url = reverse_lazy("Depot_DepotBox_list")
