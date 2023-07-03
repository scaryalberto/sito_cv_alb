import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from . import serializers
from .models import BlogArticles, GftMessages
from .forms import NewArticleForm

def home_page(request):
    return render(request, 'cv/index.html', {})



def blog_posts(request):
    posts = BlogArticles.objects.all()
    print(posts)#TODO: inserire order by date... ma al contrario (dal piu giovane al piu vecchio)
    return render(request, 'cv/blog_posts.html', {'posts': posts})

def es_gft(request):
    posts = GftMessages.objects.all()
    print(posts)
    return render(request, 'cv/gft_messages.html', {'posts': posts})

class GftView(APIView):
    """
    classe per le chiamate http
    """
    def get(self, request):
        if request.method == 'GET':
            messages = GftMessages.objects.all()
            queryset_values = messages.values()  # Ottieni una lista di dizionari
            json_data = json.dumps(list(queryset_values))  # Converti in formato JSON
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, format=None):
        """
        """
        if request.method == 'POST':
            if 'id' in request.query_params:
                record = GftMessages.objects.get(id=int(request.query_params['id']))
                # Modifica i campi desiderati
                record.tweet = request.query_params['messaggio']
                # Salva le modifiche
                record.save()

                # Restituisci una risposta o reindirizza come desiderato
                return HttpResponse("Record modificato con successo.")
            message = GftMessages(tweet=request.query_params['messaggio'])
            message.save()

            #TODO: se è presente l'id del messaggio facciamo la put
            return JsonResponse({'Success': {"message":message.id}})

def article_detail(request, id):
    post = get_object_or_404(BlogArticles, pk=id)
    return render(request, 'cv/article.html', {'post': post})

from django.shortcuts import redirect

@login_required
def create_article(request):
    context = {}

    # create object of form
    form = NewArticleForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        form.save()
        response = redirect('/blog_posts')
        return response

    context['form'] = form
    return render(request, "cv/new_article_form.html", context)