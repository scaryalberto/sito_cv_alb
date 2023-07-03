from django.contrib import admin

# Register your models here.


from django.contrib import admin
from cv.models import BlogArticles, GftMessages

admin.site.register(BlogArticles)
admin.site.register(GftMessages)
