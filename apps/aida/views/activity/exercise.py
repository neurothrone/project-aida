from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from apps.aida.forms.exercise import ExerciseForm
from apps.aida.models.activity.exercise import Exercise
from apps.aida.models.activity.workout import Workout


class List(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        context = {
            "exercises": Exercise.objects.all()
        }
        return render(request, "aida/exercise/list.html", context)


class Create(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        context = {
            "form": ExerciseForm(),
            "text": "Create Exercise",
            "workout": Workout.find_by_id(pk),
        }
        return render(request, "aida/form.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            workout = Workout.find_by_id(pk)
            exercise.workout = workout
            messages.success(request, "Exercise created.")
            return redirect("main:index")
        context = {
            "form": form,
            "text": "Create Exercise",
        }
        messages.error(request, "Failed to create exercise.")
        return render(request, "aida/form.html", context)


class Detail(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        context = {
            "exercise": Exercise.find_by_id(pk)
        }
        return render(request, "aida/exercise/detail.html", context)


class Update(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        exercise = Exercise.find_by_id(pk)
        context = {
            "form": ExerciseForm(instance=exercise),
            "text": "Update Exercise",
        }
        return render(request, "aida/form.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        exercise = Exercise.find_by_id(pk)
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            exercise = form.save()
            messages.success(request, "Exercise updated.")
            return redirect("aida:exercise-detail", pk=exercise.id)
        context = {
            "form": form,
            "text": "Update Exercise",
        }
        messages.error(request, "Failed to update exercise.")
        return render(request, "aida/form.html", context)


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        context = {
            "exercise": Exercise.find_by_id(pk),
        }
        return render(request, "aida/delete.html", context)
