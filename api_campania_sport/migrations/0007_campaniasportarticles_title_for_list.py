# Generated by Django 4.1.3 on 2022-12-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_campania_sport', '0006_campaniasportarticles_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaniasportarticles',
            name='title_for_list',
            field=models.TextField(max_length=255, null=True),
        ),
    ]