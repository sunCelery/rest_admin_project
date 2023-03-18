from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include('client.urls')),
]
