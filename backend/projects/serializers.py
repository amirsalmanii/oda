from rest_framework import serializers
from .models import Project


class ProjectSerializersM1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title_image', 'location', 'year')


class ProjectSerializersM2(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
