from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms


class AktivitetsTeamItemListView(generic.ListView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm


class AktivitetsTeamItemCreateView(generic.CreateView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm


class AktivitetsTeamItemDetailView(generic.DetailView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm


class AktivitetsTeamItemUpdateView(generic.UpdateView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm
    pk_url_kwarg = "pk"


class AktivitetsTeamItemDeleteView(generic.DeleteView):
    model = models.AktivitetsTeamItem
    success_url = reverse_lazy("AktivitetsTeam_AktivitetsTeamItem_list")


class AktivitetsTeamBookingListView(generic.ListView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AktivitetsTeamBookingCreateView(generic.CreateView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AktivitetsTeamBookingDetailView(generic.DetailView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AktivitetsTeamBookingUpdateView(generic.UpdateView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance = self.get_object()  # Pre-populate the form with object's values


class AktivitetsTeamBookingDeleteView(generic.DeleteView):
    model = models.AktivitetsTeamBooking
    success_url = reverse_lazy("AktivitetsTeam_AktivitetsTeamBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
