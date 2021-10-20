from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views import generic

from apps.aida.models.activity.exercise import Exercise
from apps.aida.models.activity.set.cardio import CardioSet
from apps.aida.models.activity.set.weight import WeightSet


# base
class SetCreate(generic.CreateView):
    context_object_name = "set"
    template_name = "aida/generic/form.html"

    # TODO: duplicated, find a way to write this only once (same work Sleep, Workout, Exercise
    def get_success_url(self):
        pk = self.kwargs["pk"]
        exercise = Exercise.find_by_id(pk)
        return exercise.get_absolute_url()

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.instance.exercise = Exercise.find_by_id(pk)
        messages.success(self.request, "Set created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Set.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(SetCreate, self).get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class SetUpdate(generic.UpdateView):
    context_object_name = "set"
    template_name = "aida/generic/form.html"

    def form_valid(self, form):
        messages.success(self.request, "Set updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Set.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(SetUpdate, self).get_context_data(**kwargs)
        context["action"] = "Update"
        return context


# defined


class CardioCreate(SetCreate):
    model = CardioSet
    queryset = CardioSet.find_all()
    fields = ("speed", "duration", "time_unit")


class CardioDetail(generic.DetailView):
    model = CardioSet
    context_object_name = "set"
    template_name = "aida/activity/set/cardio_detail.html"


class CardioUpdate(SetUpdate):
    model = CardioSet
    fields = ("speed", "duration", "time_unit")

    def get_success_url(self):
        pk = self.kwargs["pk"]
        cardio_set = CardioSet.find_by_id(pk)
        return cardio_set.exercise.get_absolute_url()


class CardioDelete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        cardio_set = CardioSet.find_by_id(pk)
        context = {
            "object": cardio_set,
            "type": "cardio set",
        }
        return render(request, "aida/generic/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        cardio_set = CardioSet.find_by_id(pk)
        if cardio_set:
            exercise_id = cardio_set.exercise.id
            cardio_set.delete()
            messages.success(request, "Set deleted.")
            return redirect("aida:exercise-detail", pk=exercise_id)
        context = {
            "object": cardio_set,
            "type": "cardio set",
        }
        messages.error(request, "Failed to delete Set.")
        return render(request, "aida/generic/delete.html", context)


class WeightCreate(SetCreate):
    model = WeightSet
    fields = ("reps", "weight", "weight_unit")


class WeightDetail(generic.DetailView):
    model = WeightSet
    context_object_name = "set"
    template_name = "aida/activity/set/weight_detail.html"


class WeightUpdate(SetUpdate):
    model = WeightSet
    fields = ("reps", "weight", "weight_unit")

    def get_success_url(self):
        pk = self.kwargs["pk"]
        weight_set = WeightSet.find_by_id(pk)
        return weight_set.exercise.get_absolute_url()


class WeightDelete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        weight_set = WeightSet.find_by_id(pk)
        context = {
            "object": weight_set,
            "type": "weight set",
        }
        return render(request, "aida/generic/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        weight_set = WeightSet.find_by_id(pk)
        if weight_set:
            exercise_id = weight_set.exercise.id
            weight_set.delete()
            messages.success(request, "Set deleted.")
            return redirect("aida:exercise-detail", pk=exercise_id)
        context = {
            "object": weight_set,
            "type": "weight set",
        }
        messages.error(request, "Failed to delete Set.")
        return render(request, "aida/generic/delete.html", context)
