from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availability_user")

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    date = models.DateField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availability_slots")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.skill} - {self.user.username}"



class HelpRequest(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="help_requests")
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} needs help with {self.skill} on {self.date}"
