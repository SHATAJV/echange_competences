from datetime import date
from django.test import TestCase

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from unittest.mock import Mock
from .models import Skill, TimeSlot, HelpRequest, Reservation


@pytest.mark.django_db
class TestSkillModel:
    """
    Tests for the Skill model, ensuring proper creation and user relationships.
    """

    def test_create_skill(self):
        """
        Test creating a Skill instance and verifying its fields.
        """
        user = User.objects.create(username="test_user")
        skill = Skill.objects.create(name="Python", user=user)

        assert skill.name == "Python"
        assert skill.user == user
        assert str(skill) == "Python"

    def test_skill_user_relationship(self):
        """
        Test the relationship between Skill and User, ensuring skills are linked
        to the correct users.
        """
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        skill1 = Skill.objects.create(name="Django", user=user1)
        skill2 = Skill.objects.create(name="React", user=user2)

        assert skill1.user == user1
        assert skill2.user == user2
        assert user1.availability_user.first() == skill1
        assert user2.availability_user.first() == skill2


@pytest.mark.django_db
class TestTimeSlotModel:
    """
    Tests for the TimeSlot model, verifying time slot creation and relationships
    with Skill and User.
    """

    def test_create_timeslot(self):
        """
        Test creating a TimeSlot instance and verifying its fields.
        """
        user = User.objects.create(username="test_user")
        skill = Skill.objects.create(name="Python", user=user)
        date = timezone.now().date()
        timeslot = TimeSlot.objects.create(date=date, skill=skill, user=user, is_available=True)

        assert timeslot.date == date
        assert timeslot.skill == skill
        assert timeslot.user == user
        assert timeslot.is_available
        assert str(timeslot) == f"{date} - {skill} - {user.username}"

    def test_timeslot_skill_user_relationship(self):
        """
        Test the relationships between TimeSlot, Skill, and User, ensuring that
        time slots are linked correctly to specific skills and users.
        """
        user = User.objects.create(username="test_user")
        skill = Skill.objects.create(name="JavaScript", user=user)
        timeslot = TimeSlot.objects.create(date=timezone.now().date(), skill=skill, user=user, is_available=False)

        assert timeslot.skill == skill
        assert timeslot.user == user
        assert not timeslot.is_available
        assert user.availability_slots.first() == timeslot


@pytest.mark.django_db
class TestHelpRequestModel:
    """
    Tests for the HelpRequest model, verifying creation and relationships with Skill and User.
    """

    def test_create_help_request(self):
        """
        Test creating a HelpRequest instance and verifying its fields.
        """
        user = User.objects.create(username="test_user")
        skill = Skill.objects.create(name="Python", user=user)
        date = timezone.now().date()
        description = "Need help with Python async code."
        help_request = HelpRequest.objects.create(skill=skill, user=user, date=date, description=description)

        assert help_request.skill == skill
        assert help_request.user == user
        assert help_request.date == date
        assert help_request.description == description
        assert str(help_request) == f"{user.username} needs help with {skill} on {date}"

    def test_help_request_skill_user_relationship(self):
        """
        Test the relationships between HelpRequest, Skill, and User, ensuring that
        help requests are linked correctly to specific skills and users.
        """
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        skill1 = Skill.objects.create(name="HTML", user=user1)
        skill2 = Skill.objects.create(name="CSS", user=user2)
        help_request1 = HelpRequest.objects.create(skill=skill1, user=user1, date=timezone.now().date(),
                                                   description="Need HTML help.")
        help_request2 = HelpRequest.objects.create(skill=skill2, user=user2, date=timezone.now().date(),
                                                   description="Need CSS help.")

        assert help_request1.skill == skill1
        assert help_request1.user == user1
        assert help_request2.skill == skill2
        assert help_request2.user == user2
        assert user1.help_requests.first() == help_request1
        assert user2.help_requests.first() == help_request2
"""
    def test_create_help_request_with_mock_skill(self):
        
        Test creating a HelpRequest instance using a mocked Skill instance to
        simulate a skill object without storing it in the database.
        
        user = User.objects.create(username="test_user")


        mock_skill = Mock()
        mock_skill.name = "MockedSkill"

        date = timezone.now().date()
        description = "Need help with a mock skill."

       
        help_request = HelpRequest(skill=mock_skill, user=user, date=date, description=description)

        assert help_request.skill == mock_skill
        assert help_request.user == user
        assert help_request.date == date
        assert help_request.description == description
        assert str(help_request) == f"{user.username} needs help with {mock_skill} on {date}"
"""

@pytest.mark.django_db
def test_reservation_creation():

    user_1 = User.objects.create_user(username="user1", password="testpassword123")
    user_2 = User.objects.create_user(username="user2", password="testpassword456")

    skill = Skill.objects.create(name="Python", user=user_1)

    time_slot = TimeSlot.objects.create(
        date=date.today(),
        skill=skill,
        user=user_1,
        is_available=True
    )

    reservation = Reservation.objects.create(
        time_slot=time_slot,
        user=user_2
    )

    assert reservation.time_slot == time_slot
    assert reservation.user == user_2
    assert reservation.time_slot.skill.name == "Python"
    assert str(reservation) == f"user2 reserved Python on {time_slot.date}"


@pytest.mark.django_db
def test_home_view(client):
    """
    Test the home view to ensure it retrieves and displays available skills and time slots.
    """
    user = User.objects.create_user(username='testuser', password='password123')
    skill = Skill.objects.create(name='Python', user=user)
    TimeSlot.objects.create(date='2024-11-16', skill=skill, user=user, is_available=True)
    response = client.get(reverse('allo_aide:home'))
    assert response.status_code == 200
    assert 'Python' in response.content.decode()

