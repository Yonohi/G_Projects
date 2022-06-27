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