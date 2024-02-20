from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from . import models
from . import forms


class AktivitetsTeamItemListView(generic.ListView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = models.AktivitetsTeamItem.objects.all().order_by('name')  # Order by the 'name' field
        return queryset


class AktivitetsTeamItemCreateView(generic.CreateView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm


class AktivitetsTeamItemDetailView(generic.DetailView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm


class AktivitetsTeamItemUpdateView(generic.UpdateView):
    model = models.AktivitetsTeamItem
    form_class = forms.AktivitetsTeamItemForm
    pk_url_kwarg = "pk"


class AktivitetsTeamItemDeleteView(generic.DeleteView):
    model = models.AktivitetsTeamItem
    success_url = reverse_lazy("AktivitetsTeam_AktivitetsTeamItem_list")


class AktivitetsTeamBookingListView(generic.ListView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm
    template_name = 'aktivitetsteambooking_list.html.html' 

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return models.AktivitetsTeamBooking.objects.order_by(F('item'),F('start_date') )


class AktivitetsTeamBookingCreateView(generic.CreateView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aktivitetsteam_items = models.AktivitetsTeamItem.objects.all()
        context['aktivitetsteam_items'] = aktivitetsteam_items
        return context


class AktivitetsTeamBookingDetailView(generic.DetailView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AktivitetsTeamBookingUpdateView(generic.UpdateView):
    model = models.AktivitetsTeamBooking
    form_class = forms.AktivitetsTeamBookingForm
    pk_url_kwarg = "pk"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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



class AktivitetsTeamBookingDeleteView(generic.DeleteView):
    model = models.AktivitetsTeamBooking
    success_url = reverse_lazy("AktivitetsTeam_AktivitetsTeamBooking_list")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
