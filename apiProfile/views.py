from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProfileUserSerializer
from .models import Profile
# Create your views here.


class CustomJTWSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        credentials = {
            "username": "",
            "password": attrs.get("password")
        }
        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(username=attrs.get("username")).first()
        if user_obj:
            credentials["username"] = user_obj.username
        return super().validate(credentials)


class ProfileUser(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user_django= request.user
        user = Profile.objects.get(user = user_django)
        user_serializer= ProfileUserSerializer(user)
        return Response({
            'data':user_serializer.data,
        })

    def post(self,request):
        user_django= request.user
        user = Profile.objects.get(user = user_django)
        data=request.data
        user_serializer= ProfileUserSerializer(user, data=data)  
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                 {'data':user_serializer.data,
                 'message': 'Información actualizada con éxito' })
        else:
            errors = user_serializer.errors
        return Response(
                        {'data':errors,
                        'message': 'ERROR' })
    