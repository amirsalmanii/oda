from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Project
from . import serializers


class ListCreateProjectView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializers


class DetailUpdateDeleteProjectView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializers
