from django import forms
from .models import Skill, TimeSlot


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']


class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['date', 'skill']
