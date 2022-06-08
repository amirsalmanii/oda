from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView, UpdateAPIView
from .models import News
from . import serializers


class ListNewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializersM2


class CreateNewsView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializers


class DetailDeleteNewstView(RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializersM2


class UpdateNewstView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializers
