from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import User
from .serializer import UserSerializer


def api_methods(request):
    return HttpResponse(
        'API methods list: not Implemented yet'
    )

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer