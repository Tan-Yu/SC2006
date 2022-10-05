from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"

class Location(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"

class Stall(models.Model):
    owner = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="stalls")
    foods = models.ManyToManyField(Food,related_name="stalls")
    def __str__(self):
        return f"Owner: {self.owner} Name: {self.name} Location: {self.location} Menu: {self.foods.all()}"
    
class Review(models.Model):
    stall=models.ForeignKey(Stall, on_delete=models.CASCADE, related_name="reviews")
    owner = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(default=None)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])