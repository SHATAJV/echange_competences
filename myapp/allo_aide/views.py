from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SkillForm
from .models import Skill, TimeSlot, HelpRequest


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
                return redirect('allo_aide:home_user')
    else:
        form = AuthenticationForm()

    return render(request, 'allo_aide/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('allo_aide:home')


def create_new_skill(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allo_aide:home_user')
    else:
        form = SkillForm()
    return render(request, 'allo_aide/create_new_skill.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    skills = Skill.objects.filter(user=user)
    help_requests = HelpRequest.objects.filter(user=user)
    time_slots = TimeSlot.objects.filter(user=user)

    context = {
        'skills': skills,
        'help_requests': help_requests,
        'time_slots': time_slots,
    }

    return render(request, 'allo_aide/dashboard.html', context)