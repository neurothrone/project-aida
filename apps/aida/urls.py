from django.urls import path

from apps.aida.views import IndexView

from apps.aida.views.activity import exercise
from apps.aida.views.activity import workout
from apps.aida.views.activity import set
from apps.aida.views.health import bloodpressure as bp
from apps.aida.views.health import heartrate as hr
from apps.aida.views.health import sleep

app_name = "aida"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    # ACTIVITY
    # - Workout
    path("workout/list/", workout.List.as_view(), name="workout-list"),
    path("workout/create/", workout.Create.as_view(), name="workout-create"),
    path("workout/detail/<int:pk>/", workout.Detail.as_view(), name="workout-detail"),
    path("workout/update/<int:pk>/", workout.Update.as_view(), name="workout-update"),
    path("workout/delete/<int:pk>/", workout.Delete.as_view(), name="workout-delete"),

    # - Exercise
    # path("exercise/list/", exercise.List.as_view(), name="exercise-list"),
    path("exercise/create/<int:pk>/", exercise.Create.as_view(), name="exercise-create"),
    path("exercise/detail/<int:pk>/", exercise.Detail.as_view(), name="exercise-detail"),
    path("exercise/update/<int:pk>/", exercise.Update.as_view(), name="exercise-update"),
    path("exercise/delete/<int:pk>/", exercise.Delete.as_view(), name="exercise-delete"),

    # - Set
    path("set/cardio/create/<int:pk>/", set.CardioCreate.as_view(), name="cardio-set-create"),
    path("set/cardio/detail/<int:pk>/", set.CardioDetail.as_view(), name="cardio-set-detail"),
    path("set/cardio/update/<int:pk>/", set.CardioUpdate.as_view(), name="cardio-set-update"),
    path("set/cardio/delete/<int:pk>/", set.CardioDelete.as_view(), name="cardio-set-delete"),

    path("set/weight/create/<int:pk>/", set.WeightCreate.as_view(), name="weight-set-create"),
    path("set/weight/detail/<int:pk>/", set.WeightDetail.as_view(), name="weight-set-detail"),
    path("set/weight/update/<int:pk>/", set.WeightUpdate.as_view(), name="weight-set-update"),
    path("set/weight/delete/<int:pk>/", set.WeightDelete.as_view(), name="weight-set-delete"),

    # HEALTH
    # - Blood pressure
    path("health/bp/list/", bp.List.as_view(), name="bp-list"),
    path("health/bp/create/", bp.Create.as_view(), name="bp-create"),
    path("health/bp/detail/<int:pk>/", bp.Detail.as_view(), name="bp-detail"),
    path("health/bp/update/<int:pk>/", bp.Update.as_view(), name="bp-update"),
    path("health/bp/delete/<int:pk>/", bp.Delete.as_view(), name="bp-delete"),

    # - Heart rate
    path("health/hr/list/", hr.List.as_view(), name="hr-list"),
    path("health/hr/create/", hr.Create.as_view(), name="hr-create"),
    path("health/hr/detail/<int:pk>/", hr.Detail.as_view(), name="hr-detail"),
    path("health/hr/update/<int:pk>/", hr.Update.as_view(), name="hr-update"),
    path("health/hr/delete/<int:pk>/", hr.Delete.as_view(), name="hr-delete"),

    # - Sleep
    path("health/sleep/load/", sleep.LoadLocalDataView.as_view(), name="sleep-load-data"),
    path("health/sleep/list/", sleep.List.as_view(), name="sleep-list"),
    path("health/sleep/create/", sleep.Create.as_view(), name="sleep-create"),
    path("health/sleep/detail/<int:pk>/", sleep.Detail.as_view(), name="sleep-detail"),
    path("health/sleep/update/<int:pk>/", sleep.Update.as_view(), name="sleep-update"),
    path("health/sleep/delete/<int:pk>/", sleep.Delete.as_view(), name="sleep-delete"),
]
