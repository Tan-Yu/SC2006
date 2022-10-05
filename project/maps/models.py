from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Coordinates(models.Model):
    name = models.CharField(max_length=128)
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    def __str__(self):
        return f"{self.name}"