from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.decorators import method_decorator

from django.contrib import messages
from . import models
from . import forms
from organization.models import EventMembership, Event
from django.utils import timezone
from django.shortcuts import render, redirect

# HTMX
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin

class SjakBookingListView(generic.ListView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm
    template_name = 'Sjak/SjakBooking_list.html'
    

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = self.request.user

            # Check the user's Event Memberships
            event_memberships = user.eventmembership_set.all()
            print("User's Event Memberships:", event_memberships)

            # Filter events by user and is_active
            active_events = user.events.filter(is_active=True)
            print("Active Events:", active_events)

            context['active_events'] = active_events
            return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)


    
class SjakBookingCreateView(SuccessMessageMixin, FormView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm
    template_name = 'Sjak/sjakbooking_form.html'
    success_url = reverse_lazy("Sjak_SjakBooking_list")
    success_message = "Form submitted successfully! Item: %(item)s"  # Add success message here


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

    def form_valid(self, form):
        form.instance.event = self.request.user.event_set.filter(is_active=True).first()  # Set the active event based on the user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance = self.get_object()  # Pre-populate the form with object's values
        
        # Add the following lines to ensure related fields are initialized
        form.fields["team"].initial = form.instance.team
        form.fields["item"].initial = form.instance.item
        form.fields["team_contact"].initial = form.instance.team_contact
        
        return form


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


class SjakBookingListView(generic.ListView):
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


@login_required
def search_item(request):
    search_text = request.POST.get('search')
    results = models.SjakItem.objects.filter(name__icontains=search_text)
    context = {"results": results}
    return render(request, 'Sjak/partials/search-results.html', context)

def clear(request):
    return HttpResponse("")
