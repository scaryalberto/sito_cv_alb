import datetime

from django.db import models

# Create your models here.

from django.db import models

class CampaniaSportArticles(models.Model):#post del blog mio
  title = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)
  date = models.DateField(default=datetime.date.today)
  image = models.ImageField(null=True, upload_to='image/')
  text = models.TextField(null=True)

  def __str__(self):
    return self.title


# posts / models.py

from django.db import models

class ArticlesToCampaniaSport(models.Model):#api per campaniasport
    title = models.TextField()
    body = models.TextField()
    image_url = models.URLField(default='http://www.campaniasport.it/')
    source = models.CharField(max_length=200) #es. www.campaniasport.it

    def __str__(self):
        return self.source


class Monuments(models.Model):
    name = models.TextField()
    description = models.TextField()
    image_url = models.URLField()
    city_location = models.CharField(max_length=200) #es. Caserta

    def __str__(self):
        return self.name + self.city_location



