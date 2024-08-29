from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from . import models
from . import forms
from django.contrib import messages
from organization.models import EventMembership, Event
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from geopy.geocoders import Nominatim


class AktivitetsTeamItemListView(LoginRequiredMixin, generic.ListView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.AktivitetsTeamItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class AktivitetsTeamItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm


class AktivitetsTeamItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm


class AktivitetsTeamItemUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm
    pk_url_kwarg = "pk"


class AktivitetsTeamItemDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.AktivitetsTeamItem
    success_url = reverse_lazy("AktivitetsTeam_AktivitetsTeamItem_list")


@login_required
@user_passes_test(lambda u: u.is_staff)
def approve_booking(request, pk):
    booking = get_object_or_404(models.AktivitetsTeamBooking, pk=pk)
    booking.status = 'Approved'
    booking.save()
    next_url = request.GET.get('next', 'AktivitetsTeam_AktivitetsTeamBooking_list')
    return redirect(next_url)

@login_required
@user_passes_test(lambda u: u.is_staff)
def reject_booking(request, pk):
    booking = get_object_or_404(models.AktivitetsTeamBooking, pk=pk)
    booking.status = 'Rejected'
    booking.save()
    next_url = request.GET.get('next', 'AktivitetsTeam_AktivitetsTeamBooking_list')
    return redirect(next_url)





class AktivitetsTeamBookingListView(LoginRequiredMixin, generic.ListView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm
    template_name = 'aktivitetsteambooking_list.html.html' 

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return models.AktivitetsTeamBooking.objects.order_by(F('item'),F('start_date') )


class AktivitetsTeamBookingCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        self.item_id = kwargs.get('item_id')

        if event and event.deadline_aktivitetsteam < timezone.now().date():
            messages.error(request, 'Deadline for booking overskredet')
            return redirect('AktivitetsTeam_AktivitetsTeamBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.item_id:
            item = get_object_or_404(models.AktivitetsTeamItem, id=self.item_id)
            kwargs['initial'] = {'item': item}
        return kwargs

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aktivitetsteam_items = models.AktivitetsTeamItem.objects.all()
            # Check if self.object exists
        if hasattr(self, 'object') and self.object is not None:
            context['object_dict'] = self.object.to_dict()
        else:
            # Provide default values for object_dict
            context['object_dict'] = {
                'latitude': '56.114951',  # Replace with your default latitude
                'longitude': '9.655592'  # Replace with your default longitude
            }
            context['aktivitetsteam_items'] = aktivitetsteam_items
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(form.cleaned_data)
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
        geolocator = Nominatim(user_agent="SKSBooking/1.0 (slettenbooking@gmail.com)")
        location = geolocator.reverse((latitude, longitude))
        print(location)
        if location:
            self.object.address = location.address
        self.object.save()
        return redirect('AktivitetsTeam_AktivitetsTeamBooking_detail', pk=self.object.pk)


class AktivitetsTeamBookingDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_dict'] = self.object.to_dict()
        latitude = context['object_dict'].get('latitude')
        longitude = context['object_dict'].get('longitude')
        
        if latitude:
            context['object_dict']['latitude'] = str(latitude).replace(',', '.')
        if longitude:
            context['object_dict']['longitude'] = str(longitude).replace(',', '.')
        
        print(context['object_dict']['latitude'])
        print(context['object_dict']['longitude'])
        return context


class AktivitetsTeamBookingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.filter(is_active=True).first()
        if event and event.deadline_aktivitetsteam < timezone.now().date():
            messages.error(request, 'Deadline for booking overskredet')
            return redirect('AktivitetsTeam_AktivitetsTeamBooking_list')  # replace with the name of your list view url
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance = self.get_object()  # Pre-populate the form with object's values
        
        # Add the following lines to ensure related fields are initialized
        form.fields["team"].initial = form.instance.team
        form.fields["item"].initial = form.instance.item
        form.fields["team_contact"].initial = form.instance.team_contact
        
        return form
    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(form.cleaned_data)
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
        latitude = str(latitude).replace(',', '.')
        longitude = str(longitude).replace(',', '.')
        geolocator = Nominatim(user_agent="SKSBooking/1.0 (slettenbooking@gmail.com)")
        
        try:
            location = geolocator.reverse((latitude, longitude))
            print(location)
            if location:
                self.object.address = location.address
        except Exception as e:
            messages.error(self.request, 'Geolocation lookup failed: {}'.format(e))
            return self.form_invalid(form)
        
        self.object.save()
        messages.success(self.request, 'Booking updated successfully')
        return redirect('AktivitetsTeam_AktivitetsTeamBooking_detail', pk=self.object.pk)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error updating the booking')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['object_dict'] = instance.to_dict()  # Ensure your model has a to_dict method
        return context


class AktivitetsTeamBookingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.AktivitetsTeamBooking
    success_url = reverse_lazy("AktivitetsTeam_AktivitetsTeamBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
