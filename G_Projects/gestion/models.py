from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


ENTREPRISE_CHOICES = [
    ('F', 'Fournisseur'),
    ('G', 'Grossiste'),
    ('P', 'Partenaire'),
]

class Teleacteur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Fournisseur(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Grossiste(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Partenaire(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Project(models.Model):
    en_cours = models.BooleanField(default=True)
    fournisseur = models.ForeignKey(to=Fournisseur,on_delete=models.SET_NULL, null=True, related_name='projets', blank=True)
    grossiste = models.ForeignKey(to=Grossiste, on_delete=models.SET_NULL, null=True, related_name='projets', blank=True)
    partenaire = models.ForeignKey(to=Partenaire, on_delete=models.SET_NULL, null=True, related_name='projets', blank=True)
    code_campagne = models.CharField(max_length=50)
    code_kammi = models.CharField(max_length=50)
    nb_jour_total = models.IntegerField(validators=[MinValueValidator(0)])
    nb_jour_realise = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    prix = models.FloatField(validators=[MinValueValidator(0)])
    date_debut = models.DateField(blank=True, null=True)
    date_fin_prevue = models.DateField(blank=True, null=True)
    date_fin_reelle = models.DateField(blank=True, null=True)
    chef_projet = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='projets')
    teleacteurs = models.ManyToManyField(Teleacteur, blank=True, related_name='projets')
    payeur = models.CharField(max_length=50, choices=ENTREPRISE_CHOICES)
    client_principal = models.CharField(max_length=50, choices=ENTREPRISE_CHOICES)
    has_objectif = models.BooleanField()
    objectif = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    def __str__(self):
        if self.client_principal == 'F':
            return f"{self.fournisseur} {self.code_campagne}".upper()
        elif self.client_principal == 'G':
            return f"{self.grossiste} {self.code_campagne}".upper()
        elif self.client_principal == 'P':
            return f"{self.partenaire} {self.code_campagne}".upper()
        else:
            return 'Erreur sur le projet'


class ToDo(models.Model):
    projet = models.OneToOneField(to=Project, on_delete=models.CASCADE)
    proposition = models.DateField(blank=True, null=True)
    commande = models.DateField(blank=True, null=True)
    brief_demarrage = models.DateField(blank=True, null=True)
    cr_brief = models.DateField(blank=True, null=True)
    script = models.DateField(blank=True, null=True)
    fichier = models.DateField(blank=True, null=True)
    rep_int = models.DateField(blank=True, null=True)
    rep_final = models.DateField(blank=True, null=True)
    facture = models.DateField(blank=True, null=True)
    reglement = models.DateField(blank=True, null=True)
    commentaire = models.TextField(blank=True)
    class Meta:
        verbose_name = 'To Do List'
        verbose_name_plural = "To Do Lists"


class Opportunite(models.Model):
    projet = models.OneToOneField(to=Project, on_delete=models.CASCADE)
    lead = models.IntegerField(default=0)
    nursering = models.IntegerField(default=0)
    fiche_info = models.IntegerField(default=0)
    commentaire = models.TextField(blank=True)
