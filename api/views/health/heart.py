from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from api.serializers.health.sleep import SleepSerializer
from aida.models.health.heart import Heart


class List(APIView):
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request: Request) -> Response:
        queryset = Heart.find_all()
        serializer = SleepSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Detail(APIView):
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request: Request, pk: int) -> Response:
        sleep = Heart.find_by_id(pk)
        if sleep:
            serializer = SleepSerializer(sleep)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ChartData(APIView):
    # authentication_classes = []
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request: Request) -> Response:
        if data := Heart.all_to_chart_data():
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
