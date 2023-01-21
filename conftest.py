import pytest
from pytest_factoryboy import register
from testing.factories import (
    CategoryFactory, 
    TeamFactory, 
    RoleFactory, 
    ProjectFactory,
    LeadFactory
)



register(CategoryFactory)
register(RoleFactory)
register(TeamFactory)
register(ProjectFactory)
register(LeadFactory)

@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }


@pytest.fixture
def project_lead_role(db, role_factory):
    lead_role = role_factory.create()
    return lead_role


@pytest.fixture
def project_lead(db, lead_factory):
    lead = lead_factory.create()
    return lead


@pytest.fixture
def project_team(db, team_factory):
    team = team_factory.create()
    return team


@pytest.fixture
def project_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture
def project_work(db, project_factory):
    project = project_factory.create()
    return project