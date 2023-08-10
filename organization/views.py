from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


User = get_user_model()



@login_required
def home(request):
	return render(request, 
		'organization/home.html', {
		})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('login_user')
    else:
        return render(request, 'organization/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)  # Use the 'user' instance, not 'User'
            messages.success(request, "Registration Successful!")
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'organization/register_user.html', {
        'form': form,
    })


class EventMembershipListView(generic.ListView):
    model = models.EventMembership
    form_class = forms.EventMembershipForm


class EventMembershipCreateView(generic.CreateView):
    model = models.EventMembership
    form_class = forms.EventMembershipForm


class EventMembershipDetailView(generic.DetailView):
    model = models.EventMembership
    form_class = forms.EventMembershipForm


class EventMembershipUpdateView(generic.UpdateView):
    model = models.EventMembership
    form_class = forms.EventMembershipForm
    pk_url_kwarg = "pk"


class EventMembershipDeleteView(generic.DeleteView):
    model = models.EventMembership
    success_url = reverse_lazy("organization_EventMembership_list")


class EventListView(generic.ListView):
    model = models.Event
    form_class = forms.EventForm


class EventCreateView(generic.CreateView):
    model = models.Event
    form_class = forms.EventForm


class EventDetailView(generic.DetailView):
    model = models.Event
    form_class = forms.EventForm


class EventUpdateView(generic.UpdateView):
    model = models.Event
    form_class = forms.EventForm
    pk_url_kwarg = "pk"


class EventDeleteView(generic.DeleteView):
    model = models.Event
    success_url = reverse_lazy("organization_Event_list")


class TeamListView(generic.ListView):
    model = models.Team
    form_class = forms.TeamForm


class TeamCreateView(generic.CreateView):
    model = models.Team
    form_class = forms.TeamForm


class TeamDetailView(generic.DetailView):
    model = models.Team
    form_class = forms.TeamForm


class TeamUpdateView(generic.UpdateView):
    model = models.Team
    form_class = forms.TeamForm
    pk_url_kwarg = "pk"


class TeamDeleteView(generic.DeleteView):
    model = models.Team
    success_url = reverse_lazy("organization_Team_list")


class TeamMembershipListView(generic.ListView):
    model = models.TeamMembership
    form_class = forms.TeamMembershipForm


class TeamMembershipCreateView(generic.CreateView):
    model = models.TeamMembership
    form_class = forms.TeamMembershipForm


class TeamMembershipDetailView(generic.DetailView):
    model = models.TeamMembership
    form_class = forms.TeamMembershipForm


class TeamMembershipUpdateView(generic.UpdateView):
    model = models.TeamMembership
    form_class = forms.TeamMembershipForm
    pk_url_kwarg = "pk"


class TeamMembershipDeleteView(generic.DeleteView):
    model = models.TeamMembership
    success_url = reverse_lazy("organization_TeamMembership_list")


class VolunteerListView(generic.ListView):
    model = models.Volunteer
    form_class = forms.VolunteerForm


class VolunteerCreateView(generic.CreateView):
    model = models.Volunteer
    form_class = forms.VolunteerForm


class VolunteerDetailView(generic.DetailView):
    model = models.Volunteer
    form_class = forms.VolunteerForm


class VolunteerUpdateView(generic.UpdateView):
    model = models.Volunteer
    form_class = forms.VolunteerForm
    pk_url_kwarg = "pk"


class VolunteerDeleteView(generic.DeleteView):
    model = models.Volunteer
    success_url = reverse_lazy("organization_Volunteer_list")