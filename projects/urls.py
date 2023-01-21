from django.urls import path
from . import views


urlpatterns = [

    path('project_detail/<int:pk>/', views.ProjectDetail.as_view()),
    path('projects_list/', views.ProjectList.as_view()),
]

