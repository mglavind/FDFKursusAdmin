from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.contrib import messages
from organization.models import EventMembership, Event
from django.utils import timezone
from django.shortcuts import redirect

class FotoItemListView(generic.ListView):
    model = models.FotoItem
    form_class = forms.FotoItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.FotoItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class FotoItemCreateView(generic.CreateView):
    model = models.FotoItem
    form_class = forms.FotoItemForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if event and event.deadline_foto < timezone.now().date():
            messages.error(request, 'Deadline for booking overskredet')
            return redirect('Foto_FotoBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs




class FotoItemDetailView(generic.DetailView):
    model = models.FotoItem
    form_class = forms.FotoItemForm


class FotoItemUpdateView(generic.UpdateView):
    model = models.FotoItem
    form_class = forms.FotoItemForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if event and event.deadline_foto < timezone.now().date():
            messages.error(request, 'Deadline for booking overskredet')
            return redirect('Foto_FotoBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)


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
