from django.contrib import admin
from .models import Location, Stall, Review, Menu
# Register your models here.

class StallAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)

    class Meta:
        model = Stall

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('owner', 'stall')

    class Meta:
        model = Review

admin.site.register(Location)
admin.site.register(Stall, StallAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Menu)
