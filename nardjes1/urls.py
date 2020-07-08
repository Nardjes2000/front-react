from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.home),
    path('article/<int:id_article>',views.article_view),
    path('accueil/',views.accueil_view),
]
