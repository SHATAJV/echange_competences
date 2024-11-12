from django.shortcuts import render
from .models import Skill, TimeSlot


def home(request):
    skills = Skill.objects.all()
    timeslots = TimeSlot.objects.filter(is_available=True)  # Affiche uniquement les créneaux disponibles
    return render(request, 'allo_aide/home.html', {'skills': skills, 'timeslots': timeslots})