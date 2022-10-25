from csv import field_size_limit
from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name','username']



class ProfileUserSerializer(serializers.Serializer):
    user = UserBaseSerializer(read_only=True)
    first_name = serializers.CharField(allow_null=True, allow_blank=True)
    last_name = serializers.CharField(allow_null=True, allow_blank=True)
    image_profile = serializers.CharField(allow_null=True, allow_blank=True)
    phone = serializers.CharField(allow_null=True, allow_blank=True)
    gender = serializers.CharField(allow_null=True, allow_blank=True)
    points = serializers.IntegerField()

    def update(self, instance, validated_data):
        user_django =instance.user
# Actualizar datos del modelo USER de django
        user_django.first_name = validated_data.get('first_name',user_django.first_name)
        user_django.last_name = validated_data.get('last_name',user_django.last_name)
# Actualizar datos de la instancia actual (Profile)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.image_profile = validated_data.get('image_profile', instance.image_profile)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.points = validated_data.get('points', instance.points)
    
        user_django.save()
        instance.save()
        return instance

    


