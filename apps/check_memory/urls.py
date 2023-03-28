from django.urls import path, include

from .views import CheckMemoryAPIView


urlpatterns = [
    path('', CheckMemoryAPIView.as_view()),
]
