# Generated by Django 4.1.3 on 2022-12-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_campania_sport', '0004_remove_campaniasportarticles_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaniasportarticles',
            name='summary',
        ),
        migrations.AlterField(
            model_name='campaniasportarticles',
            name='title',
            field=models.TextField(max_length=255),
        ),
    ]
