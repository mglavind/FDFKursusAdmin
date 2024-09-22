from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
import logging
from . import models
from . import forms
from organization.models import EventMembership, Event


# HTMX
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from organization.models import Event  # Import the Event model
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
logger = logging.getLogger(__name__)

class SjakBookingListView(LoginRequiredMixin, generic.ListView):
    model = models.SjakBooking
    form_class = forms.SjakBookingForm
    context_object_name = 'object_list'
    template_name = 'Sjak/SjakBooking_list.html'
    paginate_by = 15  # Display 15 items per page

    @method_decorator(cache_page(60 * 15))  # Cache page for 15 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = models.SjakBooking.objects.filter(
            team__in=user.teammembership_set.values('team')
        ).select_related(
            'team', 'team_contact', 'event', 'item__item_type'
        ).only(
            'id', 'team_id', 'team_contact_id', 'event_id', 'start', 'start_time', 'end', 'end_time', 'item_id', 'quantity', 'status'
        ).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        page = self.request.GET.get('page', 1)

        # Cache key based on user ID and page number
        cache_key = f'user_{user.id}_context_data_page_{page}'
        cached_context = cache.get(cache_key)

        if cached_context:
            context.update(cached_context)
            return context

        # Fetch the user's team membership
        user_team_membership = user.teammembership_set.select_related('team').first()
        is_staff = user.is_staff

        # Filter the object list based on the user's team membership and staff status
        filtered_object_list = [
            obj for obj in context['object_list']
            if (is_staff or (user_team_membership and obj.team == user_team_membership.team))
        ]

        # Fetch user events and cache them
        user_events = list(user.events.filter(is_active=True).values('name', 'deadline_sjak'))

        # Fetch volunteer team memberships and cache them
        volunteer_team_memberships = list(user.teammembership_set.select_related('team').values('team__name'))

        serializable_context = {
            'filtered_object_list': filtered_object_list,
            'is_staff': is_staff,
            'user_team_membership': user_team_membership,
            'user_events': user_events,
            'volunteer_team_memberships': volunteer_team_memberships,
        }

        context.update(serializable_context)

        try:
            # Cache the serializable context data
            cache.set(cache_key, serializable_context, 60 * 15)  # Cache for 15 minutes
        except Exception as e:
            logger.error(f"Error caching context for user {user.id} on page {page}: {e}")
        return context

    def get(self, request, *args, **kwargs):
        logger.info(f"Handling GET request for user {request.user.id} on page {self.request.GET.get('page', 1)}")
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
