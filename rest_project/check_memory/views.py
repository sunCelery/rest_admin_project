import json
import datetime
from pathlib import Path

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class CheckMemoryAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        with open(Path('/tmp/memory_info.json'), 'r') as f:
            memory_info = json.loads(f.read())
            print(memory_info)
            response = {
                "time": datetime.datetime.now(),
                **memory_info,
            }

            return Response(response)
