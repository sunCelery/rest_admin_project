from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .permissions import IsOwnerOrReadOnly
from .serializer import ClientSerializer


# class ClientAPIList(generics.ListAPIView):
#     """Returns list of clients JSON"""
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


class ClientAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

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

    def patch(self, request, *args, **kwargs):
        """
        Raises an appropriate exception if the request is not permitted
        through call check_object_permissions method
        """
        name = kwargs.get('name', None)
        if not name:
            return Response({'error': 'method PUT no allowed'})
        try:
            instance = Client.objects.get(name=name)
            self.check_object_permissions(request, instance)
        except ObjectDoesNotExist:
            return Response({'error': 'Client does not exists'})

        serializer = ClientSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({f'client updated': serializer.data})

    def delete(self, request, *args, **kwargs):
        """
        Raises an appropriate exception if the request is not permitted
        through call check_object_permissions method
        """
        name = kwargs.get('name', None)
        if not name:
            return Response({'error': 'Method DELETE not allowed'})
        try:
            instance = Client.objects.get(name=name)
            self.check_object_permissions(request, instance)
        except ObjectDoesNotExist:
            return Response({'error': 'Client does not exists'})

        instance.delete()
        return Response({'client': f'{name} deleted'})
