from django.contrib import admin
from .models import HawkerOwner, Food, Location, Stall
# Register your models here.
admin.site.register(HawkerOwner)
admin.site.register(Food)
admin.site.register(Location)
admin.site.register(Stall)
