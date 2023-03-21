from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.
class CheckMemoryAPIView(APIView):
    permission_classes = (AllowAny, )
    # renderer_classes = (JSONRenderer, )

    def get(self, request):
    #     url = 'https://archive-api.open-meteo.com/v1/era5'
    #     response = requests.get(url, params=payload)
    #     response = Response(response.json())
        response = Response({'error': 'Not Implemented yet'})
        return response
