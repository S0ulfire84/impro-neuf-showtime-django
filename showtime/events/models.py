from django.db import models
from django.core.files.storage import default_storage
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=10)
    fb_event = models.URLField(blank=True, null=True)
    ticketco = models.URLField(blank=True, null=True)
    room = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    duration_hours = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.title
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    captain_name = models.CharField(max_length=100)
    captain_email = models.EmailField()
    members = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name

class Show(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)
    team1 = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='team1_shows', blank=True, null=True)
    team2 = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='team2_shows', blank=True, null=True)
    team3 = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='team3_shows', blank=True, null=True)
    team4 = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='team4_shows', blank=True, null=True)

    def __str__(self):
        return f"Show for {self.event.title}"
    

class Workshop(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)
    leader_name = models.CharField(max_length=100)
    leader_email = models.EmailField()
    coleader_name = models.CharField(max_length=100, blank=True, null=True)
    coleader_email = models.EmailField(blank=True, null=True)
    type = models.CharField(max_length=50)
    description_internal = models.TextField()

    def __str__(self):
        return f"Workshop for {self.event.title}"
    

# This is here to delete images from Heroku, this is images, videos, etc.
def delete_team_image(team):
    if team.image:
        if hasattr(default_storage, 'delete'):
            default_storage.delete(team.image.path)
        else:
            team.image.delete()

@receiver(pre_delete, sender=Team)
def delete_image_on_team_delete(sender, instance, **kwargs):
    delete_team_image(instance)