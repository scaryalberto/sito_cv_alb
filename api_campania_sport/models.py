import datetime

from django.db import models

# Create your models here.

from django.db import models

class CampaniaSportArticles(models.Model):#post del blog mio
  title = models.TextField(max_length=255)
  image_url = models.TextField(null=True)
  text = models.TextField(null=True)
  article_url = models.TextField(null=True)
  title_for_list=models.TextField(null=True, max_length=255)

  def __str__(self):
    return self.title


# posts / models.py

from django.db import models

class Monuments(models.Model):
    name = models.TextField()
    description = models.TextField()
    image_url = models.URLField()
    city_location = models.CharField(max_length=200) #es. Caserta

    def __str__(self):
        return self.name + ' '+ self.city_location



