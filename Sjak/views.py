from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms



class SjakBookingListView(generic.ListView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class SjakBookingCreateView(generic.CreateView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SjakBookingDetailView(generic.DetailView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SjakBookingUpdateView(generic.UpdateView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SjakBookingDeleteView(generic.DeleteView):
    model = models.SjakBooking
    success_url = reverse_lazy("Sjak_SjakBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class SjakItemListView(generic.ListView):
    model = models.SjakItem
    form_class = forms.SjakItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.SjakItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class SjakItemCreateView(generic.CreateView):
    model = models.SjakItem
    form_class = forms.SjakItemForm


class SjakItemDetailView(generic.DetailView):
    model = models.SjakItem
    form_class = forms.SjakItemForm


class SjakItemUpdateView(generic.UpdateView):
    model = models.SjakItem
    form_class = forms.SjakItemForm
    pk_url_kwarg = "pk"


class SjakItemDeleteView(generic.DeleteView):
    model = models.SjakItem
    success_url = reverse_lazy("Sjak_SjakItem_list")


class SjakBookingListView(generic.ListView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm


class SjakBookingCreateView(generic.CreateView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm


class SjakBookingDetailView(generic.DetailView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm


class SjakBookingUpdateView(generic.UpdateView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm
    pk_url_kwarg = "pk"


class SjakBookingDeleteView(generic.DeleteView):
    model = models.SjakBooking
    success_url = reverse_lazy("Sjak_SjakBooking_list")


class SjakItemTypeListView(generic.ListView):
    model = models.SjakItemType
    form_class = forms.SjakItemTypeForm


class SjakItemTypeCreateView(generic.CreateView):
    model = models.SjakItemType
    form_class = forms.SjakItemTypeForm


class SjakItemTypeDetailView(generic.DetailView):
    model = models.SjakItemType
    form_class = forms.SjakItemTypeForm


class SjakItemTypeUpdateView(generic.UpdateView):
    model = models.SjakItemType
    form_class = forms.SjakItemTypeForm
    pk_url_kwarg = "pk"


class SjakItemTypeDeleteView(generic.DeleteView):
    model = models.SjakItemType
    success_url = reverse_lazy("Sjak_SjakItemType_list")
