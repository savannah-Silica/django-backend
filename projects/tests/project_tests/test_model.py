import pytest
from projects.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db

def test_lead_role(project_lead_role):
    assert project_lead_role.__str__() == 'Senior Dev'


def test_lead(project_lead):
    assert project_lead.__str__() == 'kibet@gmail.com'

def test_team(project_team):
    assert project_team.__str__() == 'A very nice team'


def test_category(project_category):
    assert project_category.__str__() == 'python'


def test_project(project_work):
    assert project_work.__str__() == 'project title'

