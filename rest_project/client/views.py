from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Client
from .serializer import ClientSerializer


def api_methods(request):
    return HttpResponse(
        'API methods list: not Implemented yet'
    )

class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
