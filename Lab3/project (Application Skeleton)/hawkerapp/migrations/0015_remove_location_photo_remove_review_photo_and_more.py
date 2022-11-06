# Generated by Django 4.1 on 2022-10-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hawkerapp", "0014_location_photo_stall_photo"),
    ]

    operations = [
        migrations.RemoveField(model_name="location", name="photo",),
        migrations.RemoveField(model_name="review", name="photo",),
        migrations.RemoveField(model_name="stall", name="photo",),
        migrations.AddField(
            model_name="location",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="review",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="stall",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]