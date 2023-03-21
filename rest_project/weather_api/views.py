from pathlib import Path

import requests
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


def get_coordinates(request: dict) -> dict:
    """
    replaces "city" from request dictionary by
    appropriate "latitude" and "longitude"
    """
    if 'city' in request:
        city = request['city']
        with open(Path('weather_api/data/cities.csv'), newline='') as csv_file:
            print(csv_file.readline())
            while True:
                csv_line = csv_file.readline()
                if city.capitalize() in csv_line:
                    _, latitude, longitude = csv_line.split(',')
                    break
            coodrinates = {
                'latitude': latitude.strip(),
                'longitude': longitude.strip(),
            }
            del request['city']
            request = {**request, **coodrinates}
            print(f"{request=}")
        return request

    else:
        return request


class WeatherAPIView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        url = 'https://archive-api.open-meteo.com/v1/era5'
        payload = {
            # 'latitude': 52.2,
            # 'longitude': 13.2,
            'start_date': '2021-01-01',
            'end_date': '2021-01-01',
            'daily': 'temperature_2m_max',
            'timezone': settings.TIME_ZONE,
        }
        payload = {**payload.copy(), **get_coordinates(request.data)}



        response = requests.get(url, params=payload)
        print(f"{type(response)=}")
        if 'error' in response.json():
            return Response({'finite': 'a la camedie'})



        response = Response(response.json())


        return response
