import csv
import json

from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.reverse import reverse as rf_reverse
import requests

from apps.aida.models.health.sleep import Sleep


class ToCSV(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": "attachment;filename=sleep_data.csv"}, )

        if data := Sleep.find_all():
            headers = ["slept_at", "awoke_at"]
            writer = csv.writer(response)
            writer.writerow(headers)
            for sleep in data:
                writer.writerow([sleep.slept_at, sleep.awoke_at])
            return response
        messages.error(request, "Failed to export data to CSV.")
        return redirect("aida:sleep-list")


class FromCSV(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        with open(settings.MEDIA_ROOT / filename, "r") as file_in:
            reader = csv.reader(file_in, delimiter=",")
            contents = [line for line in reader]
        delete_file(filename)

        if data := contents[1:]:  # [1] headers are not required
            Sleep.populate_from_csv(data)
            messages.success(request, "Sleep data successfully uploaded.")
            return redirect("aida:sleep-list")
        messages.error(request, "Failed to read data from CSV.")
        return redirect("aida:data-import")


class ToJSON(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        if data := Sleep.all_to_json():
            response = HttpResponse(
                json.dumps(data),
                content_type="application/json",
                headers={"Content-Disposition": "attachment;filename=sleep_data.json"})
            return response

        # url = rf_reverse("api:health-sleep-list", request=request)
        # r = requests.get(url, params=request.GET)
        # if r.status_code == status.HTTP_200_OK:
        #     data = r.content.decode("utf-8")
        #     response = HttpResponse(
        #         data,
        #         content_type="application/json",
        #         headers={"Content-Disposition": "attachment;filename=sleep_data.json"})
        #     return response

        messages.error(request, "Failed to export data to JSON.")
        return render(request, "aida/health/sleep/list.html")


class FromJSON(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        with open(settings.MEDIA_ROOT / filename, "r") as file_in:
            contents = json.load(file_in)
        delete_file(filename)

        if data := contents.get("data", None):
            try:
                Sleep.populate_from_json(data)
                messages.success(request, "Sleep data successfully imported.")
                return redirect("aida:sleep-list")
            except ValueError:
                messages.error(request, "Failed to decode JSON.")
        else:
            messages.error(request, "Failed to import sleep data.")
        return render(request, "aida/data/import.html")


def delete_file(filename: str) -> None:
    fs = FileSystemStorage()
    uploaded_file_path = fs.path(filename)
    fs.delete(uploaded_file_path)
