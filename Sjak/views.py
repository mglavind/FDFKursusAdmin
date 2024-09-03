from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from . import models
from . import forms
from organization.models import EventMembership, Event


# HTMX
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from organization.models import Event  # Import the Event model
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class SjakBookingListView(LoginRequiredMixin, generic.ListView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm
    context_object_name = 'object_list'
    template_name = 'Sjak/SjakBooking_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filter events by user and is_active
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    
class SjakBookingCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if event and event.deadline_sjak < timezone.now().date():
            messages.error(request, 'Booking is closed.')
            return redirect('Sjak_SjakBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sjak_items = models.SjakItem.objects.all()
        context['sjak_items'] = sjak_items
        return context
    
    def get_success_url(self):
        return reverse('Sjak_SjakBooking_detail', args=[self.object.pk])




class SjakBookingDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
@login_required
@user_passes_test(lambda u: u.is_staff)
def approve_booking(request, pk):
    booking = get_object_or_404(models.SjakBooking, pk=pk)
    booking.status = 'Approved'
    booking.save()
    next_url = request.GET.get('next', 'Sjak_SjakBooking_list')
    return redirect(next_url)

@login_required
@user_passes_test(lambda u: u.is_staff)
def reject_booking(request, pk):
    booking = get_object_or_404(models.SjakBooking, pk=pk)
    booking.status = 'Rejected'
    booking.save()
    next_url = request.GET.get('next', 'Sjak_SjakBooking_list')
    return redirect(next_url)

class SjakBookingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if event and event.deadline_sjak < timezone.now().date():
            messages.error(request, 'Booking is closed.')
            return redirect('Sjak_SjakBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sjak_items = models.SjakItem.objects.all()
        context['sjak_items'] = sjak_items
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance = self.get_object()  # Pre-populate the form with object's values
        
        # Add the following lines to ensure related fields are initialized
        form.fields["team"].initial = form.instance.team
        form.fields["item"].initial = form.instance.item
        form.fields["team_contact"].initial = form.instance.team_contact
        
        return form


class SjakBookingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.SjakBooking
    success_url = reverse_lazy("Sjak_SjakBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class SjakItemListView(generic.ListView):
    model = models.SjakItem
    form_class = forms.SjakItemForm
    context_object_name = 'object_list'
    ordering = ['name']

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


@login_required
def search_item(request):
    search_text = request.POST.get('search')
    results = models.SjakItem.objects.filter(name__icontains=search_text)
    context = {"results": results}
    return render(request, 'Sjak/partials/search-results.html', context)

def clear(request):
    return HttpResponse("")
