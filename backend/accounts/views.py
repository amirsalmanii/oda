from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from . import serializers
from .models import User


class LoginUser(APIView):
    def post(self, request):
        serializer = serializers.UserLoginRegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializers.validated_data['username']
            password = serializers.validated_data['password']
            # check user is valid or not
            user = authenticate(username=username, password=password)
            if user:
                try:
                    token = Token.objects.get(user=user)
                    Response({'token':token.key}, status=200)
                except:
                    token = Token.objects.create(user=user)
                    return Response({'token':token.key}, status=200)
            return Response(status=404)
        return Response(serializer.errors, status=400)


class ListCreateUsersView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class DetailUpdateDeleteUsersView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
