from django.contrib import admin

# Register your models here.


from django.contrib import admin
from aviation_management_system.models import *

admin.site.register(Aircrafts)
admin.site.register(Flights)