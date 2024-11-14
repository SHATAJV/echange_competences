"""
Models for representing skills, availability time slots, and help requests.

This module defines three models:
    - Skill: Represents a skill that a user can offer.
    - TimeSlot: Represents a time slot associated with a skill and availability.
    - HelpRequest: Represents a user's request for help with a specific skill.
"""

from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    """
    Model representing a specific skill a user can offer.

    Fields:
        - name: The name of the skill (must be unique).
        - user: A foreign key to the User model representing the user offering this skill.
    """
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availability_user")

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    """
    Model representing an availability time slot associated with a skill.

    Fields:
        - date: The date of the availability slot.
        - skill: A foreign key to the Skill model, linking the time slot to a specific skill.
        - user: A foreign key to the User model, representing the user available during this slot.
        - is_available: A boolean indicating if the time slot is available (default is True).
    """
    date = models.DateField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availability_slots")
    is_available = models.BooleanField(default=True)



    def __str__(self):
        return f"{self.date} - {self.skill} - {self.user.username}"


class HelpRequest(models.Model):
    """
    Model representing a help request for a specific skill on a specific date.

    Fields:
        - skill: A foreign key to the Skill model, representing the skill the user needs help with.
        - user: A foreign key to the User model, representing the user requesting help.
        - date: The date for which help is requested.
        - description: A text field allowing the user to provide additional details.
    """
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="help_requests")
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} needs help with {self.skill} on {self.date}"
