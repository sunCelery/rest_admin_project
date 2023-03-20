from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

#     path('client/', ClientAPIView.as_view()),
#     path('client/list/', ClientAPIView.as_view()),
#
#     path('client/change/', ClientAPIChange.as_view()),
#     path('client/<str:name>/', ClientAPIChange.as_view()),
#
#     path('register/', ClientAPIRegistrationView.as_view()),
]
