from django.shortcuts import render, redirect
from .models import Coordinates
from .forms import *
import folium

# Create your views here.

def coordinates_form(request):
    coordinates = Coordinates.objects.all()
    form = CoordinatesForm()

    if request.method == 'POST':
        form = CoordinatesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("maps")
    context = {
        'coordinates': coordinates,
        'form' : form,
    }
    return render(request, 'maps/maps_form.html', context)

def maps(request):
    coordinates = list(Coordinates.objects.all())

    # hawker_geojson = "hawker-centres-geojson.geojson"

    map = folium.Map(location = (1.3483, 103.6831))
    
    for coordinate in coordinates:
        # print(coordinate)
        folium.Marker([coordinate.lat, coordinate.lon], popup = coordinate.name, tooltip = coordinate.name).add_to(map)
    
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    folium.LayerControl().add_to(map)

    # folium.GeoJson(hawker_geojson, name = "geojson").add_to(map)
    # folium.LayerControl().add_to(map)
    


    map = map._repr_html_()
    context = {
        'map': map,

    }
    return render(request, 'maps/maps.html', context)