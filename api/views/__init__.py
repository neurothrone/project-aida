from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView


class RoutesView(APIView):
    @staticmethod
    def get(request: Request, *args, **kwargs) -> Response:
        routes = [
            {"GET": "/api/health/heart/"},
            {"GET": "/api/health/heart/pk/"},
            {"GET": "/api/health/heart/chart/"},
            {"GET": "/api/health/sleep/"},
            {"GET": "/api/health/sleep/pk/"},
            {"GET": "/api/health/sleep/chart/"},
        ]
        return Response(routes)
