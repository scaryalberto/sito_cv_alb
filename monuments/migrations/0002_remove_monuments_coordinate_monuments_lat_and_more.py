# Generated by Django 4.1.3 on 2023-07-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monuments", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="monuments",
            name="coordinate",
        ),
        migrations.AddField(
            model_name="monuments",
            name="lat",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="monuments",
            name="long",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
