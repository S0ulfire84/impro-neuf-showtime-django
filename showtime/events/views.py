from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Show, Team, Workshop
from .forms import ShowForm, TeamForm, WorkshopForm

###################
#      HOME       #
###################
@login_required
def home(request):
    return render(request, 'home.html')

###################
#     SHOWS       #
###################

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
    return render(request, 'shows/show_list.html', context)

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
    return render(request, 'shows/add_show.html', context)

# Edit Show
@login_required
def edit_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    if request.method == 'POST':
        form = ShowForm(request.POST, request.FILES, instance=show)
        if form.is_valid():
            form.save()
            return redirect('show_list')
    else:
        form = ShowForm(instance=show)
    return render(request, 'shows/edit_show.html', {'form': form, 'show_id': show_id})

# Remove Show
@login_required
def remove_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    if request.method == 'POST':
        show.delete()
        return redirect('show_list')
    return render(request, 'shows/remove_show.html', {'show': show})


###################
#   WORKSHOPS     #
###################

def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshops/workshop_list.html', {'workshops': workshops})

def add_workshop(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('workshop_list')
    else:
        form = WorkshopForm()
    return render(request, 'workshops/add_workshop.html', {'form': form})

def edit_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES, instance=workshop)
        if form.is_valid():
            form.save()
            return redirect('workshop_list')
    else:
        form = WorkshopForm(instance=workshop)
    return render(request, 'workshops/edit_workshop.html', {'form': form, 'workshop_id': workshop_id})

def remove_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    if request.method == 'POST':
        workshop.delete()
        return redirect('workshop_list')
    return render(request, 'workshops/remove_workshop.html', {'workshop': workshop})

###################
#      TEAMS      #
###################

# Team List
@login_required
def team_list(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'teams/team_list.html', context)

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
    return render(request, 'teams/add_team.html', context)

# Edit Team
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
    return render(request, 'teams/edit_team.html', context)

# Remove Team
@login_required
def remove_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'teams/remove_team.html', {'team': team})