from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views import View

from apps.aida.models.training.workout import Workout


class IndexView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/index.html")


class ListView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/list.html")


class DetailView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/detail.html")


class CreateView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/create.html")

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        pass


class WorkoutListView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        workouts = Workout.objects.all()
        context = {
            "workouts": workouts
        }
        return render(request, "aida/workout/list.html", context)


class WorkoutCreateView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/workout/create.html")

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        pass


class WorkoutDetailView(View):
    @staticmethod
    def get(request: HttpRequest, _id: str) -> HttpResponse:
        return render(request, "aida/workout/detail.html")
