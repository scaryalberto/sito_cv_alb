from django.db import models

# Create your models here.


from django.db import models

class Aircrafts(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name


class Flights(models.Model):
   _from = models.CharField(max_length = 10)
   _from_coordinate = models.TextField(blank=True)
   to = models.CharField(max_length = 10)
   _to_coordinate = models.TextField(blank=True)
   starting_datetime = models.DateTimeField()
   end_datetime = models.DateTimeField()
   aircraft_name = models.ForeignKey(Aircrafts, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
      return self._from+" -> "+self.to +" | "+ str(self.starting_datetime)[:10]

