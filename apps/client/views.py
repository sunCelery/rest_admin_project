from rest_framework import viewsets

from .models import CustomUser
from .permissions import IsOwnerOrReadOnly
from .serializer import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsOwnerOrReadOnly, )
