from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views import View
from django.urls import reverse_lazy

from apps.aida.models.health.heartrate import HeartRate


class List(generic.ListView):
    model = HeartRate
    context_object_name = "heartrates"
    queryset = HeartRate.find_all()
    template_name = "aida/health/heartrate/list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context["title"] = "Heart rate data"
        return context


class Create(generic.CreateView):
    model = HeartRate
    context_object_name = "hr"
    template_name = "aida/generic/form.html"
    fields = ("measured_at", "pulse")
    success_url = reverse_lazy("aida:hr-list")

    def form_valid(self, form):
        messages.success(self.request, "Heart rate data created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Heart rate data.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class Detail(generic.DetailView):
    model = HeartRate
    context_object_name = "hr"
    template_name = "aida/health/heartrate/detail.html"


class Update(generic.UpdateView):
    model = HeartRate
    context_object_name = "hr"
    template_name = "aida/generic/form.html"
    fields = ("measured_at", "pulse")
    success_url = reverse_lazy("aida:hr-list")

    def form_valid(self, form):
        messages.success(self.request, "Heart rate data updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Heart rate data.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context["action"] = "Update"
        return context


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        hr = HeartRate.find_by_id(pk)
        context = {
            "object": hr,
            "type": "heart rate",
        }
        return render(request, "aida/generic/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        hr = HeartRate.find_by_id(pk)
        if hr:
            hr.delete()
            messages.success(request, "Heart rate data deleted.")
            return redirect("aida:hr-list")
        context = {
            "object": hr,
            "type": "heart rate",
        }
        messages.error(request, "Failed to delete Heart rate data.")
        return render(request, "aida/generic/delete.html", context)
