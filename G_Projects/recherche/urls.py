from django.urls import path
from . import views

app_name = 'recherche'
urlpatterns = [
    path("recherche/", views.home_recherche, name="home_recherche"),
]