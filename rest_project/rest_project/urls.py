from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import settings

urlpatterns = [


    path('admin/', admin.site.urls),
    # path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include('client.urls')),
    path('api/v1/weather/', include('weather_api.urls')),
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)