from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from apps.aida.forms.workout import WorkoutForm
from apps.aida.models.training.workout import Workout


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
        form = WorkoutForm()
        context = {
            "form": form,
            "text": "Create Workout",
        }
        return render(request, "aida/form.html", context)

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            messages.success(request, "Workout created.")
            return redirect("aida:workout-detail", pk=workout.id)
        context = {
            "form": form,
            "text": "Create Workout",
        }
        messages.error(request, "Failed to create workout.")
        return render(request, "aida/form.html", context)


class WorkoutDetailView(View):
    @staticmethod
    def get(request: HttpRequest, pk: str) -> HttpResponse:
        context = {
            "workout": Workout.objects.filter(id=pk).first()
        }
        return render(request, "aida/workout/detail.html", context)


class WorkoutUpdateView(View):
    @staticmethod
    def get(request: HttpRequest, pk: str) -> HttpResponse:
        workout = Workout.objects.filter(id=pk).first()
        form = WorkoutForm(instance=workout)
        context = {
            "form": form,
            "text": "Update Workout",
        }
        return render(request, "aida/form.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: str) -> HttpResponse:
        workout = Workout.objects.filter(id=pk).first()
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, "Workout updated.")
            return redirect("aida:workout-list")
        context = {
            "form": form,
            "text": "Update Workout",
        }
        messages.error(request, "Failed to update workout.")
        return render(request, "aida/form.html", context)


class WorkoutDeleteView(View):
    @staticmethod
    def get(request: HttpRequest, pk: str) -> HttpResponse:
        workout = Workout.objects.filter(id=pk).first()
        context = {
            "object": f"{workout.type.title()} workout",
            "text": "Delete workout",
        }
        return render(request, "aida/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: str) -> HttpResponse:
        workout = Workout.objects.filter(id=pk).first()
        if workout:
            workout.delete()
            messages.success(request, "Workout deleted.")
            return redirect("aida:workout-list")
        context = {
            "object": f"{workout.type.title()} workout",
            "text": "Delete workout",
        }
        messages.error(request, "Failed to delete workout.")
        return render(request, "aida/delete.html", context)