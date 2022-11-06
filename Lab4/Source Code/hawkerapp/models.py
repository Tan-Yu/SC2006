# from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class Menu(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

class Location(models.Model):
    name = models.CharField(max_length=128)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return f"{self.name}"

class Stall(models.Model):
    owner = models.CharField(max_length=128)
    name=models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="stalls")
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    menus = models.ManyToManyField(Menu, related_name="stalls")

    
class Review(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    stall=models.ForeignKey(Stall, on_delete=models.CASCADE, related_name="reviews")
    owner = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(default=None)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])