from django.urls import path

from .views import IndexView
from .views import ListView
from .views import DetailView
from .views import CreateView


app_name = "aida"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("aida/list/", ListView.as_view(), name="list"),
    path("aida/detail/", DetailView.as_view(), name="detail"),
    path("aida/create/", CreateView.as_view(), name="create"),
]
