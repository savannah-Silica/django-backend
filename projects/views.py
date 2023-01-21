from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Project
from.serializers import ProjectSerializer
from rest_framework import status, generics
from rest_framework.response import Response



class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
