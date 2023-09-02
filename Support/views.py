from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms



class SupportBookingListView(generic.ListView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class SupportBookingCreateView(generic.CreateView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SupportBookingDetailView(generic.DetailView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SupportBookingUpdateView(generic.UpdateView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SupportBookingDeleteView(generic.DeleteView):
    model = models.SupportBooking
    success_url = reverse_lazy("Support_SupportBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class SupportItemListView(generic.ListView):
    model = models.SupportItem
    form_class = forms.SupportItemForm
    context_object_name = 'object_list'
    ordering = ['name']

    def get_queryset(self):
        queryset = models.SupportItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class SupportItemCreateView(generic.CreateView):
    model = models.SupportItem
    form_class = forms.SupportItemForm


class SupportItemDetailView(generic.DetailView):
    model = models.SupportItem
    form_class = forms.SupportItemForm


class SupportItemUpdateView(generic.UpdateView):
    model = models.SupportItem
    form_class = forms.SupportItemForm
    pk_url_kwarg = "pk"


class SupportItemDeleteView(generic.DeleteView):
    model = models.SupportItem
    success_url = reverse_lazy("Support_SupportItem_list")


class SupportBookingListView(generic.ListView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm


class SupportBookingCreateView(generic.CreateView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm


class SupportBookingDetailView(generic.DetailView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm


class SupportBookingUpdateView(generic.UpdateView):
    model = models.SupportBooking
    form_class = forms.SupportBookingForm
    pk_url_kwarg = "pk"


class SupportBookingDeleteView(generic.DeleteView):
    model = models.SupportBooking
    success_url = reverse_lazy("Support_SupportBooking_list")


class SupportItemTypeListView(generic.ListView):
    model = models.SupportItemType
    form_class = forms.SupportItemTypeForm


class SupportItemTypeCreateView(generic.CreateView):
    model = models.SupportItemType
    form_class = forms.SupportItemTypeForm


class SupportItemTypeDetailView(generic.DetailView):
    model = models.SupportItemType
    form_class = forms.SupportItemTypeForm


class SupportItemTypeUpdateView(generic.UpdateView):
    model = models.SupportItemType
    form_class = forms.SupportItemTypeForm
    pk_url_kwarg = "pk"


class SupportItemTypeDeleteView(generic.DeleteView):
    model = models.SupportItemType
    success_url = reverse_lazy("Support_SupportItemType_list")
