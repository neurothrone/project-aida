from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views import generic

from aida.models.activity.exercise import Exercise
from aida.models.activity.workout import Workout


class List(generic.ListView):
    model = Exercise
    context_object_name = "exercise"
    queryset = Exercise.find_all()
    template_name = "aida/activity/exercise/list.html"


class Create(generic.CreateView):
    model = Exercise
    context_object_name = "exercise"
    template_name = "aida/generic/form.html"
    fields = ("type", "name", "vest_weight")

    def get_success_url(self):
        pk = self.kwargs["pk"]
        workout = Workout.find_by_id(pk)
        return workout.get_absolute_url()

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.instance.workout = Workout.find_by_id(pk)
        messages.success(self.request, "Exercise created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Exercise.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class Detail(generic.DetailView):
    model = Exercise
    context_object_name = "exercise"
    template_name = "aida/activity/exercise/detail.html"


class Update(generic.UpdateView):
    model = Exercise
    context_object_name = "exercise"
    template_name = "aida/generic/form.html"
    fields = ("type", "name", "vest_weight")

    def get_success_url(self):
        pk = self.kwargs["pk"]
        exercise = Exercise.find_by_id(pk)
        return exercise.workout.get_absolute_url()

    def form_valid(self, form):
        messages.success(self.request, "Exercise updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Exercise.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context["action"] = "Update"
        return context


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        exercise = Exercise.find_by_id(pk)
        context = {
            "object": exercise,
            "type": "exercise",
        }
        return render(request, "aida/generic/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        exercise = Exercise.find_by_id(pk)
        if exercise:
            workout_id = exercise.workout.id
            exercise.delete()
            messages.success(request, "Exercise deleted.")
            return redirect("aida:workout-detail", pk=workout_id)
        context = {
            "object": exercise,
            "type": "exercise",
        }
        messages.error(request, "Failed to delete Exercise.")
        return render(request, "aida/generic/delete.html", context)
