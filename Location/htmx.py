from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse
from django.views import generic
from django.template import Template, RequestContext
from django.template.response import TemplateResponse

from . import models
from . import forms


class HTMXLocationTypeListView(generic.ListView):
    model = models.LocationType
    form_class = forms.LocationTypeForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXLocationTypeCreateView(generic.CreateView):
    model = models.LocationType
    form_class = forms.LocationTypeForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXLocationTypeDeleteView(generic.DeleteView):
    model = models.LocationType
    success_url = reverse_lazy("Location_LocationType_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXLocationBookingListView(generic.ListView):
    model = models.LocationBooking
    form_class = forms.LocationBookingForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXLocationBookingCreateView(generic.CreateView):
    model = models.LocationBooking
    form_class = forms.LocationBookingForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXLocationBookingDeleteView(generic.DeleteView):
    model = models.LocationBooking
    success_url = reverse_lazy("Location_LocationBooking_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXLocationItemListView(generic.ListView):
    model = models.LocationItem
    form_class = forms.LocationItemForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXLocationItemCreateView(generic.CreateView):
    model = models.LocationItem
    form_class = forms.LocationItemForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXLocationItemDeleteView(generic.DeleteView):
    model = models.LocationItem
    success_url = reverse_lazy("Location_LocationItem_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()
