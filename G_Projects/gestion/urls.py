from django.urls import path
from . import views

app_name = 'gestion'
urlpatterns = [
    path("", views.home_view, name="home"),
    path("en_cours/", views.en_cours_view, name="en_cours"),
    path("finis/", views.finis_view, name="finis"),
    path("teleacteurs/", views.teleacteurs_view, name="teleacteurs"),
    path("projet/<str:code_campagne>/", views.detail_view, name='detail'),
    path("nouveau_projet/", views.new_project_view, name='new'),
]
