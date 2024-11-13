"""
Forms for handling Skill and TimeSlot model data in forms.

"""

from django import forms
from .models import Skill, TimeSlot, HelpRequest


class SkillForm(forms.ModelForm):
    """
    A form for creating and updating Skill instances.

    Fields:
        - name: The name of the skill.
        - user: The user associated with the skill.
    """
    class Meta:
        model = Skill
        fields = ['name', 'user']


class TimeSlotForm(forms.ModelForm):
    """
    A form for creating and updating TimeSlot instances.

    Fields:
        - date: The date of the time slot.
        - skill: The skill associated with the time slot.
        - user: The user who created the time slot.
    """
    class Meta:
        model = TimeSlot
        fields = ['date', 'skill', 'user']
class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['skill', 'date', 'user','description']