from django.urls import path
from . import views

app_name = 'recherche'
urlpatterns = [
    path("", views.home_recherche, name="home_recherche"),
    path("projet/<str:code_campagne>/", views.detail_view, name='detail'),
    path("nouveau_projet/", views.new_project, name='new'),
]