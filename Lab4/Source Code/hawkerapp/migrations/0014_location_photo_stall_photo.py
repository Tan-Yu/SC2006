# Generated by Django 4.1 on 2022-10-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hawkerapp", "0013_location_rating_stall_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="photo",
            field=models.ImageField(default=0, upload_to="images"),
        ),
        migrations.AddField(
            model_name="stall",
            name="photo",
            field=models.ImageField(default=0, upload_to="images"),
        ),
    ]
