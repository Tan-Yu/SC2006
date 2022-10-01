from django.db import models

# Create your models here.


class HawkerOwner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Food(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"

class Location(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"

class Stall(models.Model):
    owner = models.ForeignKey(HawkerOwner, on_delete=models.CASCADE, related_name="stalls")
    name=models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="stalls")
    foods = models.ManyToManyField(Food,related_name="stalls")
    def __str__(self):
        return f"Owner: {self.owner} Name: {self.name} Location: {self.location} Menu: {self.foods.all()}"
    
