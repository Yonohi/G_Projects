from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Teleacteur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Client(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Project(models.Model):
    en_cours = models.BooleanField()
    client = models.ForeignKey(to=Client,on_delete=models.SET_NULL, null=True, related_name='projets')
    code_campagne = models.CharField(max_length=50)
    code_kammi = models.CharField(max_length=50)
    nb_jour_total = models.IntegerField(validators=[MinValueValidator(0)])
    nb_jour_realise = models.IntegerField(validators=[MinValueValidator(0)])
    prix = models.FloatField(validators=[MinValueValidator(0)])
    date_debut = models.DateField()
    date_fin = models.DateField()
    chef_projet = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='projets')
    teleacteurs = models.ManyToManyField(Teleacteur, blank=True)

    def __str__(self):
        return f"Projet {self.client} {self.code_campagne}"


class Lead(models.Model):
    entreprise = models.CharField(max_length=50)
    info = models.CharField(max_length=50)


class Nursering(models.Model):
    entreprise = models.CharField(max_length=50)
    info = models.CharField(max_length=50)


class FicheInfo(models.Model):
    entreprise = models.CharField(max_length=50)
    info = models.CharField(max_length=50)