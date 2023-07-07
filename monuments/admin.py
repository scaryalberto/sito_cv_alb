from django.contrib import admin

# Register your models here.


from django.contrib import admin
from monuments.models import Monuments

admin.site.register(Monuments)
