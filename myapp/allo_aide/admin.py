"""
Admin interface configuration for the application's models.

This module registers the Skill, TimeSlot, and HelpRequest models with the

"""

from django.contrib import admin
from .models import Skill, TimeSlot, HelpRequest, Reservation

admin.site.register(Skill)


admin.site.register(TimeSlot)


admin.site.register(HelpRequest)


admin.site.register(Reservation)