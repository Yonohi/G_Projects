from django.shortcuts import render
from .models import Project, Teleacteur, Lead, Nursering, FicheInfo


def home_view(request):
    projects = Project.objects.all()
    teleacteurs = Teleacteur.objects.all()
    context = {'projects': projects, 'teleacteurs': teleacteurs}
    return render(request, template_name='gestion/home.html', context=context)
