# views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib import messages
from organization.models import Todo, Team, Event, Key, TeamMembership, EventMembership
from organization.forms import TodoForm
from Butikken.models import ButikkenBooking
from Teknik.models import TeknikBooking
from Sjak.models import SjakBooking
from Foto.models import FotoBooking
from Depot.models import DepotBooking
from AktivitetsTeam.models import AktivitetsTeamBooking
from Support.models import SupportBooking


@login_required
def index(request):

    team_membership = TeamMembership.objects.filter(member=request.user).select_related('team').first()
    event_membership = EventMembership.objects.filter(volunteer=request.user).select_related('event').first()
    team = team_membership.team if team_membership else None
    print(team)
    event = event_membership.event if event_membership else None
    print(event)

    butikken_bookings = ButikkenBooking.objects.select_related('team', 'team_contact', 'item').filter(team=team)
    teknik_bookings = TeknikBooking.objects.select_related('team', 'team_contact', 'item').filter(team=team)
    sjak_bookings = SjakBooking.objects.select_related('team', 'team_contact', 'item').filter(team=team)
    foto_bookings = FotoBooking.objects.select_related('team', 'team_contact', 'item').filter(team=team)
    depot_bookings = DepotBooking.objects.select_related('team', 'team_contact', 'item').filter(team=team)
    aktivitets_team_bookings = AktivitetsTeamBooking.objects.select_related('team', 'team_contact', 'item').filter(team=team)
    support_bookings = SupportBooking.objects.select_related('team', 'team_contact', 'item').filter(team=team)

        # Get all Key objects where the current_user has a foreign key to a user that has a foreign key relation to a TeamMembership object that also has a Team value with a foreign key to the same team as the current user
    keys = Key.objects.filter(current_user__in=TeamMembership.objects.filter(team=team).values('member'))


    context = {
        'todos': Todo.objects.filter(user=request.user),
        'form': TodoForm(),
        'team': team,
        'event': event,
        'butikken_bookings': butikken_bookings,
        'teknik_bookings': teknik_bookings,
        'sjak_bookings': sjak_bookings,
        'foto_bookings': foto_bookings,
        'depot_bookings': depot_bookings,
        'aktivitets_team_bookings': aktivitets_team_bookings,
        'support_bookings': support_bookings,
        'keys': keys,
        
    }
    return render(request, 'index.html', context)

@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        # return an HTML partial
        context = {'todo': todo}
        return render(request, 'index.html#todoitem-partial', context)

@login_required
@require_POST
def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = True 
    todo.save()
    context = {'todo': todo}
    return render(request, 'index.html#todoitem-partial', context)    

@login_required
@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'delete-todo'
    return response