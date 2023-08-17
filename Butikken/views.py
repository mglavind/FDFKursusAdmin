from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ButikkenItemListView(generic.ListView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm


class ButikkenItemCreateView(generic.CreateView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm


class ButikkenItemDetailView(generic.DetailView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm


class ButikkenItemUpdateView(generic.UpdateView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm
    pk_url_kwarg = "pk"


class ButikkenItemDeleteView(generic.DeleteView):
    model = models.ButikkenItem
    success_url = reverse_lazy("Butikken_ButikkenItem_list")


class ButikkenBookingListView(generic.ListView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ButikkenBookingCreateView(generic.CreateView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ButikkenBookingDetailView(generic.DetailView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ButikkenBookingUpdateView(generic.UpdateView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    pk_url_kwarg = "pk"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ButikkenBookingDeleteView(generic.DeleteView):
    model = models.ButikkenBooking
    success_url = reverse_lazy("Butikken_ButikkenBooking_list")
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ButikkenItemTypeListView(generic.ListView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm


class ButikkenItemTypeCreateView(generic.CreateView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm


class ButikkenItemTypeDetailView(generic.DetailView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm


class ButikkenItemTypeUpdateView(generic.UpdateView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm
    pk_url_kwarg = "pk"


class ButikkenItemTypeDeleteView(generic.DeleteView):
    model = models.ButikkenItemType
    success_url = reverse_lazy("Butikken_ButikkenItemType_list")
