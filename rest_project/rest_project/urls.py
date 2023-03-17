from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView

from client.views import api_methods, ClientAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('client.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
]
