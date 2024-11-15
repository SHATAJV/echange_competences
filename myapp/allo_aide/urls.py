# Allô_aide/urls.py
from django.urls import path
from . import views

app_name = 'allo_aide'

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.home_user, name='home_user'),
    # page de connexion
    path('login/', views.login_view, name='login'),
    # ... (faire le lien avec les spécifications fonctionnelles)
    path('logout/', views.logout_view, name='logout'),
    path('create-new-skill/', views.create_new_skill, name='create_new_skill'),
    path('create-new-demande/', views.create_new_request, name='create_new_demande'),
    path('create-new-proposition/', views.create_new_proposition, name='create_new_proposition'),
    path('find-slots/<int:skill_id>/<str:date>/', views.find_slots, name='find_slots'),
    path('reserve-slot/<int:slot_id>/', views.reserve_slot, name='reserve_slot'),
    path('history/', views.history, name='history'),
]
