from django.contrib import admin
from .models import Category, Project, Lead_Role, Lead, Team

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Lead_Role)
admin.site.register(Lead)
admin.site.register(Team)