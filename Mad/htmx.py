from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse
from django.views import generic
from django.template import Template, RequestContext
from django.template.response import TemplateResponse

from . import models
from . import forms


class HTMXMadItemListView(generic.ListView):
    model = models.MadItem
    form_class = forms.MadItemForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXMadItemCreateView(generic.CreateView):
    model = models.MadItem
    form_class = forms.MadItemForm
    
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


class HTMXMadItemDeleteView(generic.DeleteView):
    model = models.MadItem
    success_url = reverse_lazy("Mad_MadItem_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXMadKategoriListView(generic.ListView):
    model = models.MadKategori
    form_class = forms.MadKategoriForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXMadKategoriCreateView(generic.CreateView):
    model = models.MadKategori
    form_class = forms.MadKategoriForm
    
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


class HTMXMadKategoriDeleteView(generic.DeleteView):
    model = models.MadKategori
    success_url = reverse_lazy("Mad_MadKategori_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXMadBookingListView(generic.ListView):
    model = models.MadBooking
    form_class = forms.MadBookingForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXMadBookingCreateView(generic.CreateView):
    model = models.MadBooking
    form_class = forms.MadBookingForm
    
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


class HTMXMadBookingDeleteView(generic.DeleteView):
    model = models.MadBooking
    success_url = reverse_lazy("Mad_MadBooking_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()
