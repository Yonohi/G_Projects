from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from .models import Project, ToDo, Teleacteur, Opportunite
from .forms import ProjectForm, FournisseurForm, GrossisteForm, PartenaireForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

@login_required
def home_view(request):
    if request.method == "POST":
        if 'projet_fini' in request.POST:
            projet_id = request.POST.get('projet_fini')
            projet = Project.objects.get(id=projet_id)
            projet.en_cours = False
            projet.save()
            return redirect('gestion:home')
        elif 'projet_reprise' in request.POST:
            projet_id = request.POST.get('projet_reprise')
            projet = Project.objects.get(id=projet_id)
            projet.en_cours = True
            projet.save()
            return redirect('gestion:home')
    user = get_user(request)
    projets_en_cours = Project.objects.filter(en_cours=True, chef_projet=user)
    projets_finis = Project.objects.filter(en_cours=False, chef_projet=user)
    context = {'projets_en_cours': projets_en_cours,
               'projets_finis': projets_finis,
               }
    return render(request, template_name='gestion/home.html', context=context)

@login_required
def en_cours_view(request):
    if request.method == "POST":
        if 'projet_fini' in request.POST:
            projet_id = request.POST.get('projet_fini')
            projet = Project.objects.get(id=projet_id)
            projet.en_cours = False
            projet.save()
            return redirect('gestion:en_cours')
    users = set(User.objects.all())
    projets_en_cours = Project.objects.filter(en_cours=True)
    chefs_en_cours = set([projet.chef_projet for projet in projets_en_cours])
    context = {'users': users,
               'projets_en_cours': projets_en_cours,
               'chefs_en_cours': chefs_en_cours,
               }
    return render(request, template_name='gestion/en_cours.html', context=context)

@login_required
def finis_view(request):
    if request.method == "POST":
        if 'projet_reprise' in request.POST:
            projet_id = request.POST.get('projet_reprise')
            projet = Project.objects.get(id=projet_id)
            projet.en_cours = True
            projet.save()
            return redirect('gestion:finis')
    users = set(User.objects.all())
    projets_finis = Project.objects.filter(en_cours=False)
    chefs_finis = set([projet.chef_projet for projet in projets_finis])
    context = {'users': users,
               'projets_finis': projets_finis,
               'chefs_finis': chefs_finis
               }
    return render(request, template_name='gestion/finis.html', context=context)

@login_required
def teleacteurs_view(request):
    teleacteurs = Teleacteur.objects.all()
    context = {'teleacteurs': teleacteurs}
    return render(request, template_name='gestion/teleacteurs.html', context=context)

@login_required
def detail_view(request, code_campagne):
    projet = Project.objects.get(code_campagne=code_campagne)
    to_do = ToDo.objects.get(projet=projet)
    opportunite = Opportunite.objects.get(projet=projet)
    context = {'projet': projet, 'to_do': to_do, 'opp': opportunite}
    return render(request, template_name='gestion/project.html', context=context)

@login_required
def new_project_view(request):
    p_form = ProjectForm()
    four_form = FournisseurForm()
    gross_form = GrossisteForm()
    part_form = PartenaireForm()
    if request.method == "POST":
        if 'fournisseur_post' in request.POST:
            four_form = FournisseurForm(request.POST)
            if four_form.is_valid():
                four_form.save()
        if 'grossiste_post' in request.POST:
            gross_form = GrossisteForm(request.POST)
            if gross_form.is_valid():
                gross_form.save()
        if 'partenaire_post' in request.POST:
            part_form = PartenaireForm(request.POST)
            if part_form.is_valid():
                part_form.save()
        if 'project_post' in request.POST:
            try:
                p_form = ProjectForm(request.POST)
                if p_form.is_valid():
                    # Après discussion il peut y avoir plus de jours réalisés que prévus
                    # if p_form.cleaned_data['nb_jour_realise'] > p_form.cleaned_data['nb_jour_total']:
                    #     raise ValidationError(message='Le nombre de jours réalisés est plus grand que le nombre de jours prévus.')
                    p_form.save()
                    projet = Project.objects.get(code_campagne=p_form.cleaned_data['code_campagne'])
                    opp = Opportunite(projet=projet, lead=0, nursering=0, fiche_info=0)
                    opp.save()
                    todo = ToDo(projet=projet)
                    todo.save()
                    return redirect('/')
            except ValidationError:
                error = 'Une erreur est présente'
                context = {'projet_form': p_form,
                           'four_form': four_form,
                           'gross_form': gross_form,
                           'part_form': part_form,
                           'error': error}
                return render(request,
                              template_name='gestion/creation_proj.html',
                              context=context)
    context = {'projet_form': p_form,
               'four_form': four_form,
               'gross_form': gross_form,
               'part_form': part_form
               }
    return render(request, template_name='gestion/creation_proj.html', context=context)