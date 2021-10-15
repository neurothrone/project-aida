from django.urls import path

from .views import IndexView
from .views.workout import WorkoutListView
from .views.workout import WorkoutCreateView
from .views.workout import WorkoutDetailView
from .views.workout import WorkoutUpdateView
from .views.workout import WorkoutDeleteView
from .views.exercise import ExerciseListView
from .views.exercise import ExerciseCreateView
from .views.exercise import ExerciseDetailView
from .views.exercise import ExerciseUpdateView
from .views.exercise import ExerciseDeleteView

app_name = "aida"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    path("workout/list/", WorkoutListView.as_view(), name="workout-list"),
    path("workout/create/", WorkoutCreateView.as_view(), name="workout-create"),
    path("workout/detail/<int:pk>/", WorkoutDetailView.as_view(), name="workout-detail"),
    path("workout/update/<int:pk>/", WorkoutUpdateView.as_view(), name="workout-update"),
    path("workout/delete/<int:pk>/", WorkoutDeleteView.as_view(), name="workout-delete"),

    path("exercise/list/", ExerciseListView.as_view(), name="exercise-list"),
    path("exercise/create/<int:pk>/", ExerciseCreateView.as_view(), name="exercise-create"),
    path("exercise/detail/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
    path("exercise/update/<int:pk>/", ExerciseUpdateView.as_view(), name="exercise-update"),
    path("exercise/delete/<int:pk>/", ExerciseDeleteView.as_view(), name="exercise-delete"),
]
