from django.shortcuts import render
from rest_framework.permissions import AllowAny


# Create your views here.
class CheckMemoryAPIView:
    permission_classes = (AllowAny, )
    # renderer_classes = (JSONRenderer, )

    # def get(self, request):
    #     url = 'https://archive-api.open-meteo.com/v1/era5'
    #     response = requests.get(url, params=payload)
    #     response = Response(response.json())
    #     return response
