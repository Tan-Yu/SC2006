# Generated by Django 4.1 on 2022-10-10 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hawkerapp", "0010_review_photo"),
    ]

    operations = [
        migrations.RemoveField(model_name="review", name="photo",),
    ]