from django import forms
from .models import Show, Team

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['event', 'team1', 'team2', 'team3', 'team4']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'captain_name', 'captain_email', 'members', 'description', 'image']