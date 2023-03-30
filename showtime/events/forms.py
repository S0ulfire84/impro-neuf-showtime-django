from django import forms
from django.forms import ModelForm, DateTimeInput
from .models import Show, Workshop, Team, Event

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'
        widgets = {
            'datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = '__all__'
        widgets = {
            'datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'