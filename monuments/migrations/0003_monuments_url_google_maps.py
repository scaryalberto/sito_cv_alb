# Generated by Django 4.1.3 on 2023-07-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monuments", "0002_remove_monuments_coordinate_monuments_lat_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="monuments",
            name="url_google_maps",
            field=models.TextField(null=True),
        ),
    ]
