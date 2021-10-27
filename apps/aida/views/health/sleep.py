import csv

from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views import View
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.reverse import reverse as rf_reverse
import requests

from apps.aida.forms.file import LoadDataForm
from apps.aida.forms.file import LoadLocalDataForm
from apps.aida.models.health.sleep import Sleep
from shared.utils.file import load_data_from_json


# class LoadDataView(View):
#     @staticmethod
#     def get(request: HttpRequest) -> HttpResponse:
#         pass
#
#     @staticmethod
#     def post(request: HttpRequest) -> HttpResponse:
#         form = LoadDataForm(request.POST, request.FILES)
#         if form.is_valid():
#             print("Form is valid.")
#             data = load_data_from_json(request.FILES["file"])
#             if data:
#                 for datum in data:
#                     print(datum)
#         return redirect("aida:sleep-list")


class LoadLocalDataView(View):
    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        if path := request.POST.get("file", None):
            data = load_data_from_json(path)
            Sleep.create_from_json(data)
            messages.success(request, "Sleep data successfully loaded.")
        return redirect("aida:sleep-list")


class ToCSV(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": "attachment;filename='sleep_data.csv'"}, )

        data = Sleep.find_all()
        headers = ["slept_at", "awoke_at"]
        writer = csv.writer(response)
        writer.writerow(headers)
        for sleep in data:
            writer.writerow([sleep.slept_at, sleep.awoke_at])
        return response


class ToJSON(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        url = rf_reverse("api:health-sleep-list", request=request)
        r = requests.get(url, params=request.GET)
        if r.status_code == status.HTTP_200_OK:
            data = r.content.decode("utf-8")
            response = HttpResponse(
                data,
                content_type="application/json",
                headers={"Content-Disposition": "attachment;filename=sleep_data.json"})
            return response
        messages.error(request, "Failed to save data to JSON.")
        return render(request, "aida/health/sleep/list.html")


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
        context["form"] = LoadLocalDataForm()
        return context


class Create(generic.CreateView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/generic/form.html"
    fields = ("slept_at", "awoke_at")
    success_url = reverse_lazy("aida:sleep-list")

    def form_valid(self, form):
        messages.success(self.request, "Sleep created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Sleep.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class Detail(generic.DetailView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/health/sleep/detail.html"


class Update(generic.UpdateView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/generic/form.html"
    fields = ("slept_at", "awoke_at")
    success_url = reverse_lazy("aida:sleep-list")

    def form_valid(self, form):
        messages.success(self.request, "Sleep updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Sleep.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context["action"] = "Update"
        return context


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        sleep = Sleep.find_by_id(pk)
        context = {
            "object": sleep,
            "type": "sleep",
        }
        return render(request, "aida/generic/delete.html", context)

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
        return render(request, "aida/generic/delete.html", context)
