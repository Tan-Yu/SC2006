from hawkerapp.models import *
import csv

def run():
    with open('hawkerapp\list-of-government-markets-hawker-centres.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        # Food.objects.all().delete()
        # Location.objects.all().delete()
        # Stall.objects.all().delete()
        # Review.objects.all().delete()

        for row in reader:
            print(row)

            location, _ = Location.objects.get_or_create(name=row[1])
            food, _ = Food.objects.get_or_create(name=row[4])

            stall = Stall(owner = row[3], name = row[0], location = location)
            stall.save()