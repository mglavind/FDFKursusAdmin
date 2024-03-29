from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from datetime import datetime

from . import models
from . import forms


class LocationTypeListView(generic.ListView):
    model = models.LocationType
    form_class = forms.LocationTypeForm
    template_name = 'locationbooking_list.html'  # replace with your actual template name
    context_object_name = 'context'  # this will be used in the template to access the context

    def get_queryset(self):
        kursus_start = datetime(2023, 10, 16)  # replace with your actual start datetime
        kursus_end = datetime(2023, 10, 20)  # replace with your actual end datetime
        duration_hours = (kursus_end - kursus_start).total_seconds() / 3600
        test = "test"


        object_list = models.LocationBooking.objects.order_by('item')
        # Format the start and end times for each booking
        for booking in object_list:
            booking.start = booking.start.strftime("%Y-%m-%DT%H:%M:%S")
            booking.end = booking.end.strftime("%Y-%m-%DT%H:%M:%S")
        

        context = {
            'kursus_start': kursus_start,
            'kursus_end': kursus_end,
            'duration_hours': duration_hours,
            'object_list': object_list,
            'test' : test,
        }
        print(list(object_list))
        for booking in object_list:
            print(booking)  #

        return context




class LocationTypeCreateView(generic.CreateView):
    model = models.LocationType
    form_class = forms.LocationTypeForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user
        return kwargs


class LocationTypeDetailView(generic.DetailView):
    model = models.LocationType
    form_class = forms.LocationTypeForm


class LocationTypeUpdateView(generic.UpdateView):
    model = models.LocationType
    form_class = forms.LocationTypeForm
    pk_url_kwarg = "pk"


class LocationTypeDeleteView(generic.DeleteView):
    model = models.LocationType
    success_url = reverse_lazy("Location_LocationType_list")


class LocationBookingListView(generic.ListView):
    model = models.LocationBooking
    form_class = forms.LocationBookingForm
    def get_queryset(self):
        queryset = models.LocationBooking.objects.all().order_by('item')  # Order by the 'name' field
        return queryset


class LocationBookingCreateView(generic.CreateView):
    model = models.LocationBooking
    form_class = forms.LocationBookingForm


class LocationBookingDetailView(generic.DetailView):
    model = models.LocationBooking
    form_class = forms.LocationBookingForm


class LocationBookingUpdateView(generic.UpdateView):
    model = models.LocationBooking
    form_class = forms.LocationBookingForm
    pk_url_kwarg = "pk"


class LocationBookingDeleteView(generic.DeleteView):
    model = models.LocationBooking
    success_url = reverse_lazy("Location_LocationBooking_list")


class LocationItemListView(generic.ListView):
    model = models.LocationItem
    form_class = forms.LocationItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.LocationItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class LocationItemCreateView(generic.CreateView):
    model = models.LocationItem
    form_class = forms.LocationItemForm


class LocationItemDetailView(generic.DetailView):
    model = models.LocationItem
    form_class = forms.LocationItemForm


class LocationItemUpdateView(generic.UpdateView):
    model = models.LocationItem
    form_class = forms.LocationItemForm
    pk_url_kwarg = "pk"


class LocationItemDeleteView(generic.DeleteView):
    model = models.LocationItem
    success_url = reverse_lazy("Location_LocationItem_list")
