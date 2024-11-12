from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class requesst_help(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request_help")
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} needs help with {self.skill} on {self.date}"
