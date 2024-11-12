
from django.http import HttpResponse
from django.shortcuts import render

from myapp.Allô_aide.models import Skill


def home(request):
    skills = Skill.objects.all()
    return render(request, 'exchange/home.html', {'skills': skills})