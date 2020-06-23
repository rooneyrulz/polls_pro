from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# REGISTER SERIALIZER
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        

# LOGIN SERIALIZER
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
        