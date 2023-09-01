from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MealBooking, Meal, Day, Option, Recipe
from organization.models import TeamMembership


class ButikkenItemListView(ListView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm
    context_object_name = 'object_list'
    ordering = ['name']

    def get_queryset(self):
        queryset = models.ButikkenItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset
    
    def sort_items(request):
        sort_by = request.GET.get('sort', 'default')  # Default sorting option

        if sort_by == 'name':
            object_list = models.ButikkenItem.objects.all().order_by('name')
        else:
            object_list = models.ButikkenItem.objects.all()

        context = {
            'object_list': object_list,
        }
        return render(request, 'your_template.html', context)


class ButikkenItemCreateView(CreateView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm


class ButikkenItemDetailView(DetailView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm


class ButikkenItemUpdateView(UpdateView):
    model = models.ButikkenItem
    form_class = forms.ButikkenItemForm
    pk_url_kwarg = "pk"


class ButikkenItemDeleteView(DeleteView):
    model = models.ButikkenItem
    success_url = reverse_lazy("Butikken_ButikkenItem_list")


class ButikkenBookingListView(ListView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ButikkenBookingCreateView(CreateView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ButikkenBookingDetailView(DetailView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ButikkenBookingUpdateView(UpdateView):
    model = models.ButikkenBooking
    form_class = forms.ButikkenBookingForm
    pk_url_kwarg = "pk"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ButikkenBookingDeleteView(DeleteView):
    model = models.ButikkenBooking
    success_url = reverse_lazy("Butikken_ButikkenBooking_list")
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ButikkenItemTypeListView(ListView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm


class ButikkenItemTypeCreateView(CreateView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm


class ButikkenItemTypeDetailView(DetailView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm


class ButikkenItemTypeUpdateView(UpdateView):
    model = models.ButikkenItemType
    form_class = forms.ButikkenItemTypeForm
    pk_url_kwarg = "pk"


class ButikkenItemTypeDeleteView(DeleteView):
    model = models.ButikkenItemType
    success_url = reverse_lazy("Butikken_ButikkenItemType_list")



####### Options

class OptionListView(ListView):
    model = models.Option
    form_class = forms.OptionForm


class OptionCreateView(CreateView):
    model = models.Option
    form_class = forms.OptionForm


class OptionDetailView(DetailView):
    model = models.Option
    form_class = forms.OptionForm


class OptionUpdateView(UpdateView):
    model = models.Option
    form_class = forms.OptionForm
    pk_url_kwarg = "pk"


class OptionDeleteView(DeleteView):
    model = models.Option
    success_url = reverse_lazy("Butikken_Option_list")


###### Meal 



class MealListView(ListView):
    model = models.Meal
    form_class = forms.MealForm


class MealCreateView(CreateView):
    model = models.Meal
    form_class = forms.MealForm


class MealDetailView(DetailView):
    model = models.Meal
    form_class = forms.MealForm


class MealUpdateView(UpdateView):
    model = models.Meal
    form_class = forms.MealForm
    pk_url_kwarg = "pk"


class MealDeleteView(DeleteView):
    model = models.Meal
    success_url = reverse_lazy("Butikken_Meal_list")


###### MealBooking


class MealBookingListView(ListView):
    model = models.MealBooking
    form_class = forms.MealBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class MealBookingCreateView(CreateView):
    model = models.MealBooking
    form_class = forms.MealBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs   


class MealBookingDetailView(DetailView):
    model = models.MealBooking
    form_class = forms.MealBookingForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class MealBookingUpdateView(UpdateView):
    model = models.MealBooking
    form_class = forms.MealBookingForm
    pk_url_kwarg = "pk"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MealBookingDeleteView(DeleteView):
    model = models.MealBooking
    success_url = reverse_lazy("Butikken_MealBooking_list")




class DayListView(ListView):
    model = models.Day
    form_class = forms.DayForm


class DayCreateView(CreateView):
    model = models.Day
    form_class = forms.DayForm


class DayDetailView(DetailView):
    model = models.Day
    form_class = forms.DayForm


class DayUpdateView(UpdateView):
    model = models.Day
    form_class = forms.DayForm
    pk_url_kwarg = "pk"


class DayDeleteView(DeleteView):
    model = models.Day
    success_url = reverse_lazy("Butikken_Day_list")


class RecipeListView(ListView):
    model = models.Recipe
    form_class = forms.RecipeForm


class RecipeCreateView(CreateView):
    model = models.Recipe
    form_class = forms.RecipeForm


class RecipeDetailView(DetailView):
    model = models.Recipe
    form_class = forms.RecipeForm


class RecipeUpdateView(UpdateView):
    model = models.Recipe
    form_class = forms.RecipeForm
    pk_url_kwarg = "pk"


class RecipeDeleteView(DeleteView):
    model = models.Recipe
    success_url = reverse_lazy("Butikken_Recipe_list")
