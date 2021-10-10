from django.urls import path

from .views import WorkoutListView
from .views import WorkoutCreateView
from .views import WorkoutDetailView

app_name = "aida"
urlpatterns = [
    path("workouts/list/", WorkoutListView.as_view(), name="workouts-list"),
    path("workouts/create/", WorkoutCreateView.as_view(), name="workouts-create"),
    path("workouts/<str:id>/", WorkoutDetailView.as_view(), name="workouts-detail"),
]
