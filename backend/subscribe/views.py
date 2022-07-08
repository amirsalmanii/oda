from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Subscribe
from .serializers import SubscribeSerializer


class SubsCreateListView(ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

