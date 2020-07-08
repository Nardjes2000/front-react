from django.db import models


# Create your models here.
class malade(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    telephone=models.CharField(max_length=10) #les expression regulieres
    date_naissance=models.DateField()
    csg=models.CharField(max_length=5)



class dossier(models.Model):
   date=models.DateField()
   poids=models.CharField(max_length=20)
   taille=models.CharField(max_length=20)
   pc=models.CharField(max_length=20)
   examenclinique=models.TextField()
   malade=models.ForeignKey('malade',on_delete=models.CASCADE) #le malade du dossier en supprimant le malade le dosssier sera supprimer

class antcf(models.Model):#antecedant familail
    contenu=models.TextField()


class grocess(models.Model):

    contenu=models.TextField()
    medic=models.TextField()


class info_naissance(models.Model):

    poids =models.CharField(max_length=20)
    taille=models.CharField(max_length=20)
    pc=models.CharField(max_length=20)



class antcp(models.Model): #antecedant personel
     alt=models.TextField()
     par=models.TextField()
     vac=models.TextField()
     lait=models.TextField()
     dpm=models.TextField()
     path=models.TextField()
     thera=models.TextField()
     grocess=models.OneToOneField(grocess, on_delete=models.CASCADE)
     infos_naisssnace=models.OneToOneField(info_naissance, on_delete=models.CASCADE)


