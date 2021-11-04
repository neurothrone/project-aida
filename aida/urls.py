from django.urls import path

from aida.views import file
from aida.views import IndexView
from aida.views.activity import exercise
from aida.views.activity import workout
from aida.views.activity import set
from aida.views.health import heart as heart
from aida.views.health import sleep as sleep

app_name = "aida"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    # DATA
    path("import-data/", file.Import.as_view(), name="data-import"),

    # ACTIVITY
    # - Workout
    path("workout/list/", workout.List.as_view(), name="workout-list"),
    path("workout/create/", workout.Create.as_view(), name="workout-create"),
    path("workout/detail/<int:pk>/", workout.Detail.as_view(), name="workout-detail"),
    path("workout/update/<int:pk>/", workout.Update.as_view(), name="workout-update"),
    path("workout/delete/<int:pk>/", workout.Delete.as_view(), name="workout-delete"),

    # - Exercise
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
    # - Heart
    path("health/heart/list/", heart.crud.List.as_view(), name="heart-list"),
    path("health/heart/create/", heart.crud.Create.as_view(), name="heart-create"),
    path("health/heart/detail/<int:pk>/", heart.crud.Detail.as_view(), name="heart-detail"),
    path("health/heart/update/<int:pk>/", heart.crud.Update.as_view(), name="heart-update"),
    path("health/heart/delete/<int:pk>/", heart.crud.Delete.as_view(), name="heart-delete"),

    # - Sleep
    path("health/sleep/from-csv/<str:filename>/", sleep.data.FromCSV.as_view(),
         name="sleep-from-csv"),
    path("health/sleep/from-json/<str:filename>/", sleep.data.FromJSON.as_view(),
         name="sleep-from-json"),
    path("health/sleep/to-csv/", sleep.data.ToCSV.as_view(), name="sleep-to-csv"),
    path("health/sleep/to-json/", sleep.data.ToJSON.as_view(), name="sleep-to-json"),
    path("health/sleep/list/", sleep.crud.List.as_view(), name="sleep-list"),
    path("health/sleep/create/", sleep.crud.Create.as_view(), name="sleep-create"),
    path("health/sleep/detail/<int:pk>/", sleep.crud.Detail.as_view(), name="sleep-detail"),
    path("health/sleep/update/<int:pk>/", sleep.crud.Update.as_view(), name="sleep-update"),
    path("health/sleep/delete/<int:pk>/", sleep.crud.Delete.as_view(), name="sleep-delete"),
]
