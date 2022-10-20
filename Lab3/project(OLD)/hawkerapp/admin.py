from django.contrib import admin
from .models import Food, Location, Stall, Review
# Register your models here.
admin.site.register(Food)
admin.site.register(Location)
admin.site.register(Stall)
admin.site.register(Review)
