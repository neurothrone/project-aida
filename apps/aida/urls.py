from django.urls import path

from apps.aida.views import IndexView

from apps.aida.views.activity import exercise
from apps.aida.views.activity import workout
from apps.aida.views.health import sleep

app_name = "aida"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    # ACTIVITY
    #   Workout
    path("workout/list/", workout.List.as_view(), name="workout-list"),
    path("workout/create/", workout.Create.as_view(), name="workout-create"),
    path("workout/detail/<int:pk>/", workout.Detail.as_view(), name="workout-detail"),
    path("workout/update/<int:pk>/", workout.Update.as_view(), name="workout-update"),
    path("workout/delete/<int:pk>/", workout.Delete.as_view(), name="workout-delete"),

    #   Exercise
    path("exercise/list/", exercise.List.as_view(), name="exercise-list"),
    path("exercise/create/<int:pk>/", exercise.Create.as_view(), name="exercise-create"),
    path("exercise/detail/<int:pk>/", exercise.Detail.as_view(), name="exercise-detail"),
    path("exercise/update/<int:pk>/", exercise.Update.as_view(), name="exercise-update"),
    path("exercise/delete/<int:pk>/", exercise.Delete.as_view(), name="exercise-delete"),

    # HEALTH
    #   Sleep
    path("health/sleep/list/", sleep.List.as_view(), name="sleep-list"),
    path("health/sleep/create/", sleep.Create.as_view(), name="sleep-create"),
    path("health/sleep/detail/<int:pk>/", sleep.Detail.as_view(), name="sleep-detail"),
    path("health/sleep/update/<int:pk>/", sleep.Update.as_view(), name="sleep-update"),
    path("health/sleep/delete/<int:pk>/", sleep.Delete.as_view(), name="sleep-delete"),
]
