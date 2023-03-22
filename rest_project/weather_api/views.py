import re
from pathlib import Path

import requests
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import CityNotFoundOrNotGiven, DateNotGiven


def get_coordinates(
        request: dict,
        number_of_cities_in_db: int = 42906) -> dict:
    """
    replaces "city" from request dictionary by
    appropriate "latitude" and "longitude"
    because original API uses them
    """
    if 'city' in request:
        city = request['city']
        with open(Path('weather_api/data/cities.csv'), newline='') as csv_file:
            for _ in range(number_of_cities_in_db):
                csv_line = csv_file.readline()
                pattern = r'^' + city + r'.*,'
                if re.search(pattern, csv_line, re.IGNORECASE):
                    _, latitude, longitude = csv_line.split(',')
                    coordinates = {
                        'latitude': latitude.strip(),
                        'longitude': longitude.strip(),
                    }
                    del request['city']
                    request = {**request, **coordinates}
                    return request

    raise CityNotFoundOrNotGiven


def get_date(request: dict) -> dict:
    """
    replaces "date" from request dictionary by
    appropriate "start_date" and "end_date"
    because original API uses them
    """
    if 'date' in request:
        date = request['date'].strip()
        dates = {
            'start_date': date,
            'end_date': date,
        }
        del request['date']
        request = {**request, **dates}
        return request

    else:
        raise DateNotGiven


class WeatherAPIView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        url = 'https://archive-api.open-meteo.com/v1/era5'
        payload = {
            'daily': 'temperature_2m_max',
            'timezone': settings.TIME_ZONE,
        }
        try:
            payload = {
                **payload.copy(),
                **get_coordinates(request.data),
                **get_date(request.data),
            }
            response = requests.get(url, params=payload)
            response = Response(response.json())
            return response

        except CityNotFoundOrNotGiven:
            response = {
                'error': '"city" not given or there is no such city '
                         'in the Earth. Send city in format like:',
                'city': 'Murom',
            }
            return Response(response)

        except DateNotGiven:
            response = {
                'error': '"date" not given. Send date in format like:',
                'date': "2012-11-22",
            }
            return Response(response)
