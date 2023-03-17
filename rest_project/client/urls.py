from django.urls import path

from .views import *


urlpatterns = [
    path('methods/', api_methods),
    path('list/', ClientAPIView.as_view()),
]