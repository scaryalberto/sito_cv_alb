# Generated by Django 2.2.28 on 2022-12-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_campania_sport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesToCampaniaSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('image_url', models.URLField(default='http://www.campaniasport.it/')),
                ('source', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Monuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('city_location', models.CharField(max_length=200)),
            ],
        ),
    ]
