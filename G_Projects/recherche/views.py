from django.shortcuts import render

def home_recherche(request):
    context = {}
    return render(request, template_name='recherche/home_recherche.html', context=context)
