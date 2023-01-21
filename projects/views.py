from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Project
from.serializers import ProjectSerializer
from rest_framework import status, generics
from rest_framework.response import Response


# Create your views here.

# @api_view(['GET', 'PUT', 'DELETE'])
# def DetailView(request, id):

#     """
#     Retrieve, update or delete a project.
#     """

#     try:
#         projects = Project.objects.all(id=id)
#     except Project.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProjectSerializer(projects)
#         return Response(serializer.data)

#     elif  request.method == 'PUT':
#         serializer = ProjectSerializer(projects, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     elif request.method == 'DELETE':
#         projects.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@api_view(['GET', 'POST'])
def ListView(request):

    """
    List all projects, or create a new project.
    """

    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

