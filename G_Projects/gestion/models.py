from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    en_cours = models.BooleanField()
    code_campagne = models.CharField(max_length=50)
    code_kami = models.CharField(max_length=50)
    nb_jour_total = models.IntegerField()
    nb_jour_realise = models.IntegerField()
    prix = models.FloatField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    chef_projet = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='projets')


class Teleacteur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)


class Lead(models.Model):
    entreprise = models.CharField(max_length=50)
    info = models.CharField(max_length=50)


class Nursering(models.Model):
    entreprise = models.CharField(max_length=50)
    info = models.CharField(max_length=50)


class FicheInfo(models.Model):
    entreprise = models.CharField(max_length=50)
    info = models.CharField(max_length=50)