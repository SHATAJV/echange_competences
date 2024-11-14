from datetime import date

from django.test import TestCase

# Create your tests here.

from .models import Skill, TimeSlot


import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def skill(user):
    return Skill.objects.create(name='Python', user=user)

def test_skill_str_method(skill):
    """
    Test the __str__ method of the Skill model.
    """
    assert str(skill) == 'Python'

def test_skill_unique_name(user):
    """
    Test that the 'name' field is unique.
    """
    with pytest.raises(Exception):
        Skill.objects.create(name='Python', user=user)


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def skill(user):
    return Skill.objects.create(name='Python', user=user)

@pytest.fixture
def time_slot(user, skill):
    return TimeSlot.objects.create(date=date(2024, 11, 21), skill=skill, user=user)

def test_timeslot_str_method(time_slot):
    """
    Test the __str__ method of the TimeSlot model.
    """
    assert str(time_slot) == '2024-11-21 - Python - testuser'

def test_timeslot_availability_default(user, skill):
    """
    Test that a TimeSlot is available by default.
    """
    time_slot = TimeSlot.objects.create(date=date(2024, 11, 22), skill=skill, user=user)
    assert time_slot.is_available is True

def test_timeslot_availability_false(time_slot):
    """
    Test that we can set a TimeSlot as unavailable.
    """
    time_slot.is_available = False
    time_slot.save()
    assert time_slot.is_available is False
