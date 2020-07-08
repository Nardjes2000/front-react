from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse,Http404 
from .models import malade

# Create your views here.
def home(request):
    malades=malade.objects.all()
    return(HttpResponse("<h1>hi nardjes</h1>"))

def accueil_view(request):
      return render(request, 'nardjes/accueil.html')

def article_view(request,id_article):
    if id_article>5:
      raise Http404

    return(HttpResponse("id {0}".format(id_article)))