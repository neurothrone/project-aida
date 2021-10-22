from django.urls import path

from api.views import RoutesView
from api.views.health import sleep

app_name = "api"
urlpatterns = [
    path("", RoutesView.as_view(), name="routes"),
    path("health/sleep/", sleep.List.as_view(), name="health-sleep-list"),
    path("health/sleep/<int:pk>/", sleep.Detail.as_view(), name="health-sleep-detail"),
    path("health/sleep/chart/", sleep.ChartData.as_view(), name="health-sleep-chart"),
]
