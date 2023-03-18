from django.urls import path

from .views import *


urlpatterns = [
    path('methods/', methods),
    path('client/', ClientAPIView.as_view()),
    path('client/list/', ClientAPIView.as_view()),
    path('client/<str:name>/', ClientAPIView.as_view()),
]
