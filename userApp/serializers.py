from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'username', 'first_name', 'last_name', 'phone_number', 'role', 'is_superuser', 'phone_number',
            'gender', 'image', 'birth_date', 'address', 'date_joined'
        )

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)


class ProfileManagerSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'username', 'first_name', 'last_name', 'phone_number', 'role', 'is_superuser', 'phone_number',
            'gender', 'image', 'birth_date', 'address', 'date_joined'
        )

    def create(self, validated_data):
        profile = Profile.objects.create_user(**validated_data)
        profile.role = 'manager'
        profile.save()
        return profile


class ProfileOrdinarySerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'username', 'first_name', 'last_name', 'phone_number', 'role', 'is_superuser', 'phone_number',
            'gender', 'image', 'birth_date', 'address', 'date_joined'
        )

    def create(self, validated_data):
        profile = Profile.objects.create_user(**validated_data)
        profile.role = 'ordinary'
        profile.save()
        return profile

#
# class ProfileRegisterSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(max_length=15, min_length=9)
#     password = serializers.CharField(write_only=True, style={'input_type': 'password'}, min_length=6, max_length=32)
#
#
# class ProfileConfirmSerializer(serializers.Serializer):
#     confirmation_code = serializers.CharField(max_length=6, min_length=6)
