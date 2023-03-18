from django.urls import path, include
from rest_framework import routers

from .views import *


# router = routers.DefaultRouter()
# router.register(r'client', ClientViewSet)
# print(router.urls)

urlpatterns = [
    # path('client/list/', ClientAPIList.as_view()),
    # path('client/<str:name>/', ClientAPIView.as_view()),
    # path('client/<str:name>/', ClientAPIDestroy.as_view()),
    path('client/', ClientAPIView.as_view()),
    path('client/list/', ClientAPIView.as_view()),
    path('client/<str:name>/', ClientAPIView.as_view()),
]
