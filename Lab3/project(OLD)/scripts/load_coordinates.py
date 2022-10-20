from maps.models import Coordinates
import geojson

def run():
    with open('maps\hawker-centres-geojson.geojson') as file:
        reader = geojson.load(file)

    location = reader['features']
    for loc in location:
        coord = loc['geometry']['coordinates']
        print(coord)
        coordinate = Coordinates(lat = coord[1], lon = coord[0])
        coordinate.save()