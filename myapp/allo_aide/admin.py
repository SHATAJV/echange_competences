"""
interface admin
"""


from django.contrib import admin
from .models import Skill, TimeSlot, HelpRequest




admin.site.register(Skill)
admin.site.register(TimeSlot)
admin.site.register(HelpRequest)
