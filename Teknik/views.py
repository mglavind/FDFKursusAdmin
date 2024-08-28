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
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
@user_passes_test(lambda u: u.is_staff)
def approve_booking(request, pk):
    booking = get_object_or_404(models.TeknikBooking, pk=pk)
    booking.status = 'Approved'
    booking.save()
    next_url = request.GET.get('next', 'Teknik_TeknikBooking_list')
    return redirect(next_url)

@login_required
@user_passes_test(lambda u: u.is_staff)
def reject_booking(request, pk):
    booking = get_object_or_404(models.TeknikBooking, pk=pk)
    booking.status = 'Rejected'
    booking.save()
    next_url = request.GET.get('next', 'Teknik_TeknikBooking_list')
    return redirect(next_url)



class TeknikBookingListView(LoginRequiredMixin, generic.ListView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class TeknikBookingCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        
        if not self.request.user.is_staff and event and event.deadline_teknik < timezone.now().date():
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


class TeknikBookingDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TeknikBookingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.TeknikBooking
    form_class = forms.TeknikBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if not self.request.user.is_staff and event and event.deadline_teknik < timezone.now().date():
            messages.error(request, 'booking deadline overskredet')
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

class TeknikBookingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.TeknikBooking
    success_url = reverse_lazy("Teknik_TeknikBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TeknikItemListView(LoginRequiredMixin, generic.ListView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.TeknikItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class TeknikItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm


class TeknikItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm


class TeknikItemUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.TeknikItem
    form_class = forms.TeknikItemForm
    pk_url_kwarg = "pk"


class TeknikItemDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.TeknikItem
    success_url = reverse_lazy("Teknik_TeknikItem_list")


class TeknikTypeListView(LoginRequiredMixin, generic.ListView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm


class TeknikTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm


class TeknikTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm


class TeknikTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.TeknikType
    form_class = forms.TeknikTypeForm
    pk_url_kwarg = "pk"


class TeknikTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.TeknikType
    success_url = reverse_lazy("Teknik_TeknikType_list")
