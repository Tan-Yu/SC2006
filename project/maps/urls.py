from . import views
from django.urls import path

urlpatterns = [ 
    path('',views.maps, name = 'coordinates-form'),
    # path('map', views.maps, name = 'maps'),
]