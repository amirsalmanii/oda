from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Project
from . import serializers


class ListProjectView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializersM1


class CreateProjectView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializersM2


class DetailUpdateDeleteProjectView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializersM2
