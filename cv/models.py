import datetime

from django.db import models

# Create your models here.

from django.db import models

class BlogArticles(models.Model):
  title = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)
  date = models.DateField(default=datetime.date.today)
  image_url = models.CharField(max_length=255, null=True)
  text = models.TextField(null=True)
  #upload = models.ImageField(upload_to='uploads/')

  def __str__(self):
    return self.title


class GftMessages(models.Model):
  tweet = models.CharField(max_length=300)

  def __str__(self):
    return self.tweet

