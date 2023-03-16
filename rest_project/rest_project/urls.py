from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView

from users.views import api_methods, UserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]
