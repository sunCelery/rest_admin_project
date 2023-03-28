from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Client, CustomUser


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('birth_date', 'sex', 'photo')


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ClientSerializer(required=True)

    class Meta:
        model = CustomUser
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        Client.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.sex = profile_data.get('sex', profile.sex)
        profile.birth_date = profile_data.get('birth_date', profile.birth_date)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance
