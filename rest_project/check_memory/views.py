import datetime
from pathlib import Path

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class CheckMemoryAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        with open(Path('/tmp/memory_info.txt'), 'r') as f:
            response = {
                "time": datetime.datetime.now(),
                'memory-info': f.readline()
            }

            return Response(response)
