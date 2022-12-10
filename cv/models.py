import datetime

from django.db import models

# Create your models here.

from django.db import models

class BlogArticles(models.Model):
  title = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)
  date = models.DateField(default=datetime.date.today)
  image = models.ImageField(null=True, upload_to='image/image/')
  text = models.TextField(null=True)
  #upload = models.ImageField(upload_to='uploads/')

  def __str__(self):
    return self.title


