import datetime
from django import forms
from .models import Project, Fournisseur, Grossiste, Partenaire


class FournisseurForm(forms.ModelForm):
    fournisseur_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Fournisseur
        fields = "__all__"


class GrossisteForm(forms.ModelForm):
    grossiste_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Grossiste
        fields = "__all__"


class PartenaireForm(forms.ModelForm):
    partenaire_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Partenaire
        fields = "__all__"

class ProjectForm(forms.ModelForm):
    project_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Project
        fields = "__all__"
        # widgets = {
            # 'en_cours': forms.CheckboxInput(attrs={'class': 'form-check-input', }),
            # 'fournisseur': forms.Select(attrs={'class': 'form-control',}),
            # 'grossiste': forms.Select(attrs={'class': 'form-control', }),
            # 'partenaire': forms.Select(attrs={'class': 'form-control', }),
            # 'code_campagne': forms.TextInput(attrs={'class': 'form-control', }),
            # 'code_kammi': forms.TextInput(attrs={'class': 'form-control', }),
            # 'nb_jour_total': forms.TextInput(attrs={'class': 'form-control', 'type': 'number' }),
            # 'nb_jour_realise': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            # 'prix': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            # 'date_debut': forms.TextInput(attrs={'type': 'date' ,'class': 'form-control'}),
        # }
