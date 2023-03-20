from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import Client
from .permissions import IsOwnerOrReadOnly



from rest_framework import viewsets

from .models import CustomUser
from .serializer import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



# from .serializer import ClientSerializer, RegisterSerializer

#
# class ClientAPIRegistrationView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = (AllowAny, )
#
#
#
# class ClientAPIView(APIView):
#     permission_classes = (AllowAny, )
#
#     def get(self, request, *args, **kwargs):
#         name = kwargs.get('name', None)
#         if name:
#             try:
#                 instance = Client.objects.get(name=name)
#                 serializer = ClientSerializer(instance=instance)
#                 return Response({'client': serializer.data})
#             except ObjectDoesNotExist:
#                 return Response({'error': f'Client {name} does not exists'})
#         else:
#             clients = Client.objects.all()
#             response = Response(
#                 {'clients': ClientSerializer(clients, many=True).data}
#             )
#             return response
#
# class ClientAPIChange(APIView):
#     permission_classes = (IsAuthenticated, )
#
#     def post(self, request):
#         serializer = ClientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         response = Response(
#             {'client created': serializer.data}
#         )
#         return response
#
#     def patch(self, request, *args, **kwargs):
#         """
#         Raises an appropriate exception if the request is not permitted
#         through call check_object_permissions method
#         """
#         name = kwargs.get('name', None)
#         if not name:
#             return Response({'error': 'method PUT no allowed'})
#         try:
#             instance = Client.objects.get(name=name)
#             self.check_object_permissions(request, instance)
#         except ObjectDoesNotExist:
#             return Response({'error': 'Client does not exists'})
#
#         serializer = ClientSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({f'client updated': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         """
#         Raises an appropriate exception if the request is not permitted
#         through call check_object_permissions method
#         """
#         name = kwargs.get('name', None)
#         if not name:
#             return Response({'error': 'Method DELETE not allowed'})
#         try:
#             instance = Client.objects.get(name=name)
#             self.check_object_permissions(request, instance)
#         except ObjectDoesNotExist:
#             return Response({'error': 'Client does not exists'})
#
#         instance.delete()
#         return Response({'client': f'{name} deleted'})
