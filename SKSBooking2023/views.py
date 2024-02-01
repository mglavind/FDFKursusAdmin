# views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib import messages
from organization.models import Todo, Team, Event, TeamMembership, EventMembership
from organization.forms import TodoForm


@login_required
def index(request):

    team = TeamMembership.objects.filter(member=request.user).first().team
    event = EventMembership.objects.filter(volunteer=request.user).first().event
    print('team:', team),
    print('event:', event),

    context = {
        'todos': Todo.objects.filter(user=request.user),
        'form': TodoForm(),
        'team': team,
        'event': event,
        
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