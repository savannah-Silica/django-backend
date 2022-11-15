from django.urls import path
from . import views


urlpatterns = [
    path('projects_list/', views.ListView),
]