from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from apps.aida.forms.exercise import ExerciseForm
from apps.aida.models.activity.workout.exercise import Exercise
from apps.aida.models.activity.workout import Workout


class ExerciseListView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        context = {
            "exercises": Exercise.objects.all()
        }
        return render(request, "aida/exercise/list.html", context)


class ExerciseCreateView(View):
    @staticmethod
    def get(request: HttpRequest, pk: str) -> HttpResponse:
        context = {
            "form": ExerciseForm(),
            "text": "Create Exercise",
            "workout": Workout.objects.filter(id=pk).first()
        }
        return render(request, "aida/form.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: str) -> HttpResponse:
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            workout = Workout.objects.filter(id=pk).first()
            exercise.workout = workout
            messages.success(request, "Exercise created.")
            return redirect("main:index")
        context = {
            "form": form,
            "text": "Create Exercise",
        }
        messages.error(request, "Failed to create exercise.")
        return render(request, "aida/form.html", context)


class ExerciseDetailView(View):
    @staticmethod
    def get(request: HttpRequest, pk: str) -> HttpResponse:
        context = {
            "exercise": Exercise.objects.filter(id=pk).first()
        }
        return render(request, "aida/exercise/detail.html", context)


class ExerciseUpdateView(View):
    @staticmethod
    def get(request: HttpRequest, pk: str) -> HttpResponse:
        exercise = Exercise.objects.filter(id=pk).first()
        context = {
            "form": ExerciseForm(instance=exercise),
            "text": "Update Exercise",
        }
        return render(request, "aida/form.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: str) -> HttpResponse:
        exercise = Exercise.objects.filter(id=pk).first()
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


class ExerciseDeleteView(View):
    @staticmethod
    def get(request: HttpRequest, pk: str) -> HttpResponse:
        context = {
            "exercise": Exercise.objects.filter(id=pk).first(),
        }
        return render(request, "aida/delete.html", context)
