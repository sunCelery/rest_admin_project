import requests
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class WeatherAPIView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        url = 'https://archive-api.open-meteo.com/v1/era5'
        payload = {
            'latitude': 52.2,
            'longitude': 13.2,
            'start_date': '2021-01-01',
            'end_date': '2021-01-01',
            'daily': 'temperature_2m_max',
            'timezone': settings.TIME_ZONE,
        }

        payload = {**payload.copy(), **request.data}

        response = requests.get(url, params=payload)
        response = Response(response.json())

        return response
