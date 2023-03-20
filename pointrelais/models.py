from django.db import models

# Create your models here.

class Relaypoint(models.Model):
    quartier_id = models.IntegerField()
    img = models.CharField(max_length=300)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    localisation =  models.CharField(max_length=100)
    map_address = models.CharField(max_length=100)
    