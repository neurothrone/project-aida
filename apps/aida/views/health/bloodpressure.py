from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views import View
from django.urls import reverse_lazy

from apps.aida.models.health.bloodpressure import BloodPressure


class List(generic.ListView):
    model = BloodPressure
    context_object_name = "bloodpressures"
    queryset = BloodPressure.find_all()
    template_name = "aida/health/bloodpressure/list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context["title"] = "Blood pressure data"
        return context


class Create(generic.CreateView):
    model = BloodPressure
    context_object_name = "bp"
    template_name = "aida/generic/form.html"
    fields = ("measured_at", "systolic", "diastolic")
    success_url = reverse_lazy("aida:bp-list")

    def form_valid(self, form):
        messages.success(self.request, "Blood pressure data created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Blood pressure data.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class Detail(generic.DetailView):
    model = BloodPressure
    context_object_name = "bp"
    template_name = "aida/health/bloodpressure/detail.html"


class Update(generic.UpdateView):
    model = BloodPressure
    context_object_name = "bp"
    template_name = "aida/generic/form.html"
    fields = ("measured_at", "systolic", "diastolic")
    success_url = reverse_lazy("aida:bp-list")

    def form_valid(self, form):
        messages.success(self.request, "Blood pressure data updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Blood pressure data.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context["action"] = "Update"
        return context


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        bp = BloodPressure.find_by_id(pk)
        context = {
            "object": bp,
            "type": "blood pressure",
        }
        return render(request, "aida/generic/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        bp = BloodPressure.find_by_id(pk)
        if bp:
            bp.delete()
            messages.success(request, "Blood pressure data deleted.")
            return redirect("aida:bp-list")
        context = {
            "object": bp,
            "type": "blood pressure",
        }
        messages.error(request, "Failed to delete Blood pressure data.")
        return render(request, "aida/generic/delete.html", context)
