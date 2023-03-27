from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Show
from .forms import ShowForm

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