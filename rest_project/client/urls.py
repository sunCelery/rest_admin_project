from django.urls import path, include

from .views import *


urlpatterns = [
    path('client/', ClientAPIView.as_view()),
    path('client/list/', ClientAPIView.as_view()),
    path('client/<str:name>/', ClientAPIView.as_view()),
    path('register/', ClientAPIRegistrationView.as_view()),
]
