from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Skill, TimeSlot


def home(request):
    skills = Skill.objects.all()
    timeslots = TimeSlot.objects.filter(is_available=True)  # Affiche uniquement les créneaux disponibles
    return render(request, 'allo_aide/home.html', {'skills': skills, 'timeslots': timeslots})

@login_required
def home_user(request):
    return render(request, 'allo_aide/home_user.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('allo_aide:home_user')  # Redirige vers la page des utilisateurs connectés
    else:
        form = AuthenticationForm()

    return render(request, 'allo_aide/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('allo_aide:home')
