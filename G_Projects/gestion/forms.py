import datetime
from django import forms
from .models import Project, Fournisseur, Grossiste, Partenaire, Teleacteur


class FournisseurForm(forms.ModelForm):
    fournisseur_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Fournisseur
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', }),
        }


class GrossisteForm(forms.ModelForm):
    grossiste_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Grossiste
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', }),
        }


class PartenaireForm(forms.ModelForm):
    partenaire_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Partenaire
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', }),
        }

class ProjectForm(forms.ModelForm):
    project_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'en_cours': forms.CheckboxInput(attrs={'class': 'form-check-input', }),
            'fournisseur': forms.Select(attrs={'class': 'form-control',}),
            'grossiste': forms.Select(attrs={'class': 'form-control', }),
            'partenaire': forms.Select(attrs={'class': 'form-control', }),
            'code_campagne': forms.TextInput(attrs={'class': 'form-control', }),
            'code_kammi': forms.TextInput(attrs={'class': 'form-control', }),
            'nb_jour_total': forms.TextInput(attrs={'class': 'form-control', 'type': 'number' }),
            'nb_jour_realise': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'prix': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'date_debut': forms.TextInput(attrs={'type': 'date' ,'class': 'form-control'}),
            'date_fin_prevue': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin_reelle': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'chef_projet': forms.Select(attrs={'class': 'form-control', }),
            'teleacteurs': forms.SelectMultiple(attrs={'class': 'form-select',}),
            'payeur': forms.Select(attrs={'class': 'form-control', }),
            'client_principal': forms.Select(attrs={'class': 'form-control' }),
            'has_objectif': forms.CheckboxInput(attrs={'class': 'form-check-input', }),
            'objectif': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }
