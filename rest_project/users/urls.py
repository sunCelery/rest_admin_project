from django.urls import path

from .views import *


urlpatterns = [
    path('methods/', api_methods),
    path('list_all_users/', UserAPIView.as_view()),
]