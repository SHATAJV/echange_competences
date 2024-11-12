# Allô_aide/urls.py
from django.urls import path
from . import views

app_name = 'allo_aide'

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil pour les visiteurs
    path('user/', views.home_user, name='home_user'),  # Page d'accueil pour utilisateurs connectés
    path('login/', views.login_view, name='login'),  # Page de connexion
    path('logout/', views.logout_view, name='logout'),  # Déconnexion
]
