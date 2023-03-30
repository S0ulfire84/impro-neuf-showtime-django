from django import forms
from .models import Show, Workshop, Team

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'