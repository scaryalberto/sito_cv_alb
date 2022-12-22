# Generated by Django 4.1.3 on 2022-12-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_campania_sport', '0007_campaniasportarticles_title_for_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('vote', models.IntegerField()),
                ('text_review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrapingReviewsUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrapingReviewsWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
            ],
        ),
    ]