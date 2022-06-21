from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Project, Client, Teleacteur, Lead, Nursering, FicheInfo
from .forms import ProjectForm, ClientForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

@login_required
def home_view(request):
    users = set(User.objects.all())
    projets_en_cours = Project.objects.filter(en_cours=True)
    chefs_en_cours = set([projet.chef_projet for projet in projets_en_cours])
    projets_finis = Project.objects.filter(en_cours=False)
    chefs_finis = set([projet.chef_projet for projet in projets_finis])
    clients = set(Client.objects.all())
    context = {'users': users,
               'projets_en_cours': projets_en_cours,
               'projets_finis': projets_finis,
               'clients': clients,
               'chefs_en_cours': chefs_en_cours,
               'chefs_finis': chefs_finis
               }
    return render(request, template_name='gestion/home.html', context=context)

@login_required
def detail_view(request, code_campagne):
    project = Project.objects.get(code_campagne=code_campagne)
    context = {'project': project}
    return render(request, template_name='gestion/project.html', context=context)

@login_required
def new_project(request):
    p_form = ProjectForm()
    c_form = ClientForm()
    if request.method == "POST":
        if 'client_post' in request.POST:
            c_form = ClientForm(request.POST)
            if c_form.is_valid():
                c_form.save()
        if 'project_post' in request.POST:
            try:
                p_form = ProjectForm(request.POST)
                if p_form.is_valid():
                    # Après discussion il peut y avoir plus de jours réalisés que prévus
                    # if p_form.cleaned_data['nb_jour_realise'] > p_form.cleaned_data['nb_jour_total']:
                    #     raise ValidationError(message='Le nombre de jours réalisés est plus grand que le nombre de jours prévus.')
                    p_form.save()
                    return redirect('/')
            except ValidationError:
                error = 'Une erreur est présente'
                context = {'projet_form': p_form,
                           'client_form': c_form,
                           'error': error}
                return render(request,
                              template_name='gestion/creation_proj.html',
                              context=context)
    context = {'projet_form': p_form, 'client_form': c_form}
    return render(request, template_name='gestion/creation_proj.html', context=context)