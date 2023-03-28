from django.urls import path, include

from .views import WeatherAPIView


urlpatterns = [
    path('', WeatherAPIView.as_view()),
]
