from django import forms
from .models import Project, Client


class ClientForm(forms.ModelForm):
    client_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Client
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    project_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Project
        fields = "__all__"