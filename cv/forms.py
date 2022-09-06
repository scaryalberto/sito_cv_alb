# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import BlogArticles

# create a ModelForm
class NewArticleForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = BlogArticles
		fields = "__all__"
		exclude = ('date',)
