from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Show, Team
from .forms import ShowForm, TeamForm

# Home
@login_required
def home(request):
    return render(request, 'home.html')

# Show List
@login_required
def show_list(request):
    shows = Show.objects.all()

    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_list')
    else:
        form = ShowForm()

    context = {'shows': shows, 'form': form}
    return render(request, 'show_list.html', context)

# Add Show
@login_required
def add_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_list')
    else:
        form = ShowForm()

    context = {'form': form}
    return render(request, 'add_show.html', context)

# Team List
@login_required
def team_list(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'team_list.html', context)

# Add Team
@login_required
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()

    context = {'form': form}
    return render(request, 'add_team.html', context)

@login_required
def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)

    context = {'form': form, 'team': team}
    return render(request, 'edit_team.html', context)

@login_required
def remove_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'remove_team.html', {'team': team})