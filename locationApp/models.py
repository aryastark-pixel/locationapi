from django.db import models

class BeatPersonnelOne(models.Model):
    latitude = models.FloatField();
    longitude = models.FloatField();
    dateTime = models.DateTimeField();

# Create your models here.
