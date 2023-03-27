from django import forms
from .models import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['event', 'team1', 'team2', 'team3', 'team4']