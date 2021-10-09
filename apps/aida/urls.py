from django.urls import path

from .views import IndexView
from .views import WorkoutListView
from .views import WorkoutCreateView
from .views import WorkoutDetailView

# from .views import ListView
# from .views import DetailView
# from .views import CreateView


app_name = "aida"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("aida/workouts/list/", WorkoutListView.as_view(), name="workouts-list"),
    path("aida/workouts/create/", WorkoutCreateView.as_view(), name="workouts-create"),
    path("aida/workouts/<str:id>/", WorkoutDetailView.as_view(), name="workouts-detail"),

    # path("aida/list/", ListView.as_view(), name="list"),
    # path("aida/detail/", DetailView.as_view(), name="detail"),
    # path("aida/create/", CreateView.as_view(), name="create"),
]
