from django.db import models

# Create your models here.
class Monuments(models.Model):
  name = models.CharField(max_length=300)
  long = models.CharField(max_length=300, null=True)
  lat = models.CharField(max_length=300, null=True)
  url_image = models.CharField(max_length=300)
  description = models.TextField()

  def __str__(self):
    return self.name


