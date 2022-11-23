from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.


class Lead_Role(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    class Meta:
        verbose_name_plural = 'Lead_Roles'

    def __str__(self):
        return f'{self.title}'


class Lead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=150)
    lead_role = models.ForeignKey(Lead_Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Leads'

    def __str__(self):
        return f'{self.user}'



class Team(models.Model):
    description = models.TextField(max_length=250)
    members = models.ManyToManyField(User)
    leads = models.ManyToManyField(Lead)


    class Meta:
        verbose_name_plural = 'Teams'
    
    def __str__(self):
        return f'{self.description}'

    

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)




    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    version_control = models.URLField(max_length=250)
    repository = models.URLField(max_length=250)
    domain = models.URLField(max_length=250)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f'{self.title}'
