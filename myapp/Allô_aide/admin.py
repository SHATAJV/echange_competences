from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Skill, requesst_help


admin.site.register(Skill)
admin.site.register(requesst_help)