import factory
from faker import Faker
from projects.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


faker = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'kibet'
    email = 'kibet@gmail.com'
    native_name = 'mutai'
    phone_no = '0712345678'


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    title = 'python'
    description = 'this is python'


class RoleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Lead_Role
    
    title = 'Senior Dev'
    description = 'this is senior dev'


class TeamFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Team

    description = 'A very nice team'


class ProjectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Project

    title = 'project title'
    description = 'awesome projects built'
    category = factory.SubFactory(CategoryFactory)
    version_control = 'http://www.github.com'
    repository = 'http://www.github.com/savannah'
    domain = 'http://www.github.com/servers'
    team = factory.SubFactory(TeamFactory)

class LeadFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Lead
        # django_get_or_create = ('User',)

    user = factory.SubFactory(UserFactory)
    description = 'This is Lead factory'
    lead_role = factory.SubFactory(RoleFactory)