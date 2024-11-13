# Allô_aide/urls.py
from django.urls import path
from . import views

app_name = 'allo_aide'

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.home_user, name='home_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create-new-skill/', views.create_new_skill, name='create_new_skill'),
    path('create-new-demande/', views.create_new_request, name='create_new_demande'),
]
