from django.shortcuts import render, redirect

def home_recherche(request):
    if request.method == "POST":
        query = request.POST.get('search_input')
        return redirect('recherche:resultats', query)
    context = {}
    return render(request, template_name='recherche/home_recherche.html', context=context)

def resultats_recherche(request, query):
    if request.method == "POST":
        new_query = request.POST.get('search_input')
        return redirect('recherche:resultats', new_query)
    context = {'query': query}
    return render(request, template_name='recherche/resultats.html', context=context)