"""
Views for managing user authentication, homepage display, and skill/time slot creation.

This module defines views for user login, logout, homepage rendering, user dashboard,
and forms to create new skills and requests for time slots.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SkillForm, TimeSlotForm
from .models import Skill, TimeSlot, HelpRequest


def home(request):
    """
    View to render the homepage, displaying available skills and time slots.

    Context:
        - skills: All available skills.
        - timeslots: Available time slots marked as is_available=True.
    """
    skills = Skill.objects.all()
    timeslots = TimeSlot.objects.filter(is_available=True) 
    return render(request, 'allo_aide/home.html', {'skills': skills, 'timeslots': timeslots})


@login_required
def home_user(request):
    """
    View to render the user's home page after login. Requires the user to be logged in.
    """
    user = request.user
    skills = Skill.objects.filter(user=user)  # Fetch only the logged-in user's skills
    help_requests = HelpRequest.objects.filter(user=user)
    time_slots = TimeSlot.objects.filter(user=user)

    context = {
        'skills': skills,
        'help_requests': help_requests,
        'time_slots': time_slots,
    }
    return render(request, 'allo_aide/home_user.html', context)

def login_view(request):
    """
    View to handle user login.

    If the request is POST, processes the AuthenticationForm with POST data.
    If valid, logs the user in and redirects them to the home_user page.
    If the request is GET, displays an empty AuthenticationForm.

    Context:
        - form: Instance of AuthenticationForm for login.
    """
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
    """
    View to handle user logout, then redirects to the homepage.
    """
    logout(request)
    return redirect('allo_aide:home')


def create_new_skill(request):
    """
    View to create a new skill using SkillForm.

    If the request is POST and form is valid, saves the new skill and redirects
    to the home_user page. Otherwise, displays an empty SkillForm.

    Context:
        - form: Instance of SkillForm for creating a new skill.
    """
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            new_skill = form.save(commit=False)
            new_skill.user = request.user
            new_skill.save()
            return redirect('allo_aide:home_user')
    else:
        form = SkillForm()
    return render(request, 'allo_aide/create_new_skill.html', {'form': form})


def create_new_request(request):
    """
    View to create a new time slot demand using TimeSlotForm.

    If the request is POST and the form is valid, saves the new time slot and redirects
    to the home_user page. Otherwise, displays an empty TimeSlotForm.

    Context:
        - form: Instance of TimeSlotForm for creating a new time slot demand.
    """
    if request.method == "POST":
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allo_aide:home_user')
    else:
        form = TimeSlotForm()
    return render(request, 'allo_aide/create_new_demande.html', {'form': form})
