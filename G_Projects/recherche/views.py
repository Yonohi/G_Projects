from django.shortcuts import render, redirect
from gestion.models import Project, Fournisseur, Grossiste, Partenaire
from django.contrib.auth.decorators import login_required

@login_required
def home_recherche(request):
    if request.method == "POST":
        query = request.POST.get('search_input')
        return redirect('recherche:resultats', query)
    context = {}
    return render(request, template_name='recherche/home_recherche.html', context=context)

@login_required
def resultats_recherche(request, query):
    # Code pour la recherche avec la bd de base
    # On commence par créer une liste de mots
    words = query.split()
    resultats_four = []
    resultats_gross = []
    resultats_part = []
    resultats_code = []
    resultats_prio = []
    resultats_reste = []
    for word in words:
        fournisseurs = Fournisseur.objects.filter(nom__icontains=word)
        grossistes = Grossiste.objects.filter(nom__icontains=word)
        partenaires = Partenaire.objects.filter(nom__icontains=word)
        projets = Project.objects.filter(code_campagne__icontains=word)
        for fournisseur in fournisseurs:
            resultats_four.extend(list(fournisseur.projets.all()))
            resultats_reste.extend(resultats_four)
        for grossiste in grossistes:
            resultats_gross.extend(list(grossiste.projets.all()))
            resultats_reste.extend(resultats_gross)
        for partenaire in partenaires:
            resultats_part.extend(list(partenaire.projets.all()))
            resultats_reste.extend(resultats_part)
        resultats_code.extend(list(projets))
        resultats_reste.extend(resultats_code)
        resultats_reste = list(set(resultats_reste))
    resultats_prio.extend(list(set(resultats_code) & set(resultats_four)))
    resultats_prio.extend(list(set(resultats_code) & set(resultats_gross)))
    resultats_prio.extend(list(set(resultats_code) & set(resultats_part)))
    resultats_prio = list(set(resultats_prio))
    for elmt in resultats_prio:
        if elmt in resultats_reste:
            resultats_reste.remove(elmt)

    if request.method == "POST":
        new_query = request.POST.get('search_input')
        return redirect('recherche:resultats', new_query)
    if len(words) == 1:
        context = {'query': query, 'resultats_prio': list(set(resultats_prio) | set(resultats_reste))}
    else:
        context = {'query': query, 'resultats_prio': resultats_prio, 'resultats_reste': resultats_reste}
    return render(request, template_name='recherche/resultats.html', context=context)