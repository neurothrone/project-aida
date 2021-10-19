from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views import View
from django.urls import reverse_lazy

from apps.aida.models.health.sleep import Sleep


# TODO: set permissions
class List(generic.ListView):
    model = Sleep
    context_object_name = "sleeps"
    queryset = Sleep.find_all()
    template_name = "aida/health/sleep/list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context["title"] = "Sleep Data"
        return context


class Create(generic.CreateView):
    model = Sleep
    context_object_name = "sleep"
    queryset = Sleep.find_all()
    template_name = "aida/generic_form.html"
    fields = ("slept_at", "awoke_at")

    def form_valid(self, form):
        messages.success(self.request, "Sleep created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Sleep.")
        return super().form_invalid(form)


class Detail(generic.DetailView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/health/sleep/detail.html"


class Update(generic.UpdateView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/generic_form.html"
    fields = ("slept_at", "awoke_at")
    success_url = reverse_lazy("aida:sleep-list")

    def form_valid(self, form):
        messages.success(self.request, "Sleep updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Sleep.")
        return super().form_invalid(form)


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        sleep = Sleep.find_by_id(pk)
        context = {
            "object": sleep,
            "type": "sleep",
        }
        return render(request, "aida/generic_delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        sleep = Sleep.find_by_id(pk)
        if sleep:
            sleep.delete()
            messages.success(request, "Sleep deleted.")
            return redirect("aida:sleep-list")
        context = {
            "object": sleep,
            "type": "sleep",
        }
        messages.error(request, "Failed to delete Sleep.")
        return render(request, "aida/generic_delete.html", context)
