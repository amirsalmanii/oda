from rest_framework import serializers
from .models import News
from accounts.models import User


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class UserNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")


class NewsSerializersM2(serializers.ModelSerializer):
    author = UserNewsSerializer()
    class Meta:
        model = News
        fields = "__all__"