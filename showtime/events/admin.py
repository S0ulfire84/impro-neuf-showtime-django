from django.contrib import admin
from .models import Event, Team, Show, Workshop

# Register your models here.
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Show)
admin.site.register(Workshop)