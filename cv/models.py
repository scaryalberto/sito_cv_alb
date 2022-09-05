from django.db import models

# Create your models here.

from django.db import models

class BlogArticles(models.Model):
  title = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)
  date = models.DateField()
  image = models.ImageField()
  #upload = models.ImageField(upload_to='uploads/')

  def __str__(self):
    return self.title


