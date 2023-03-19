from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id', 'username', 'email', 'password',
            'name', 'surname', 'sex', 'birth_date',
        )
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        client = Client.onjects.create(**validated_data)
        Client.objects.create(user=client)
        return client


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
        #           'name', 'surname', 'sex', 'birth_date')
        # extra_kwargs = {
        #     'name': {'required': False},
        #     'surname': {'required': False},
        #     'sex': {'required': False},
        #     'birth_date': {'required': False},
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"error": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'].
        )

        user.set_password(validated_data['password'])
        user.save()

        return user