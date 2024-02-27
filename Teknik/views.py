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

class TeknikBookingListView(generic.ListView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class TeknikBookingCreateView(generic.CreateView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if event and event.deadline_teknik < timezone.now().date():
            messages.error(request, 'booking deadline overskredet')
            return redirect('Teknik_TeknikBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teknik_items = models.TeknikItem.objects.all()
        context['teknik_items'] = teknik_items
        return context


class TeknikBookingDetailView(generic.DetailView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TeknikBookingUpdateView(generic.UpdateView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if event and event.deadline_teknik < timezone.now().date():
            messages.error(request, 'booking deadline overskredet.')
            return redirect('Teknik_TeknikBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)

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
        return form

class TeknikBookingDeleteView(generic.DeleteView):
    model = models.TeknikBooking
    success_url = reverse_lazy("Teknik_TeknikBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TeknikItemListView(generic.ListView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.TeknikItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class TeknikItemCreateView(generic.CreateView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm


class TeknikItemDetailView(generic.DetailView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm


class TeknikItemUpdateView(generic.UpdateView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm
    pk_url_kwarg = "pk"


class TeknikItemDeleteView(generic.DeleteView):
    model = models.TeknikItem
    success_url = reverse_lazy("Teknik_TeknikItem_list")


class TeknikTypeListView(generic.ListView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm


class TeknikTypeCreateView(generic.CreateView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm


class TeknikTypeDetailView(generic.DetailView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm


class TeknikTypeUpdateView(generic.UpdateView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm
    pk_url_kwarg = "pk"


class TeknikTypeDeleteView(generic.DeleteView):
    model = models.TeknikType
    success_url = reverse_lazy("Teknik_TeknikType_list")
