from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views import View

from aida.models.activity.workout import Workout


class List(generic.ListView):
    model = Workout
    context_object_name = "workouts"
    queryset = Workout.find_all()
    template_name = "aida/activity/workout/list.html"
    paginate_by = 10


class Create(generic.CreateView):
    model = Workout
    context_object_name = "workout"
    template_name = "aida/generic/form.html"
    fields = ("type", "engaged_at",)
    success_url = reverse_lazy("aida:workout-list")

    def form_valid(self, form):
        messages.success(self.request, "Workout created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Workout.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class Detail(generic.DetailView):
    model = Workout
    context_object_name = "workout"
    template_name = "aida/activity/workout/detail.html"


class Update(generic.UpdateView):
    model = Workout
    context_object_name = "workout"
    template_name = "aida/generic/form.html"
    fields = ("type", "engaged_at")
    success_url = reverse_lazy("aida:workout-list")

    def form_valid(self, form):
        messages.success(self.request, "Workout updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Workout.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context["action"] = "Update"
        return context


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        workout = Workout.find_by_id(pk)
        context = {
            "object": workout,
            "type": "workout",
        }
        return render(request, "aida/generic/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        workout = Workout.find_by_id(pk)
        if workout:
            workout.delete()
            messages.success(request, "Workout deleted.")
            return redirect("aida:workout-list")
        context = {
            "object": workout,
            "type": "workout",
        }
        messages.error(request, "Failed to delete Workout.")
        return render(request, "aida/generic/delete.html", context)
