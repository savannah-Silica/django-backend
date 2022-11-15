from django.urls import path
from . import views


urlpatterns = [

    path('project_detail/<int:id>/', views.DetailView)


    path('projects_list/', views.ListView),
]

