from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializer import ClientSerializer


def methods(request):
    return HttpResponse(
        'API methods list: not Implemented yet'
    )



class ClientAPIView(APIView):
    def get(self, request, *args, **kwargs):
        name = kwargs.get('name', None)
        if name:
            try:
                instance = Client.objects.get(name=name)
                serializer = ClientSerializer(instance=instance)
                return Response({'client': serializer.data})
            except ObjectDoesNotExist:
                return Response({'error': f'Client {name} does not exists'})
        else:
            clients = Client.objects.all()
            response = Response(
                {'clients': ClientSerializer(clients, many=True).data}
            )
            return response

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response(
            {'client created': serializer.data}
        )
        return response

    def put(self, request, *args, **kwargs):
        name = kwargs.get('name', None)
        if not name:
            return Response({'error': 'method PUT no allowed'})
        try:
            instance = Client.objects.get(name=name)
        except:
            return Response({'error': 'Client does not exists'})

        serializer = ClientSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({f'client updated': serializer.data})

    def delete(self, request, *args, **kwargs):
        name = kwargs.get('name', None)
        if not name:
            return Response({'error': 'Method DELETE not allowed'})
        try:
            instance = Client.objects.get(name=name)
        except:
            return Response({'error': 'Client does not exists'})

        instance.delete()
        return Response({'client': f'{name} deleted'})



















# class ClientAPIView(generics.ListAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
