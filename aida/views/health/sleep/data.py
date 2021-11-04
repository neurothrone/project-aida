import csv
import json

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from aida.models.health.sleep import Sleep
from aida.views.utils import delete_file_on_server
from aida.views.utils import to_csv_response
from aida.views.utils import to_json_response


class ToCSV(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        header, data = Sleep.all_to_csv()
        return to_csv_response("sleep_data", header, data)


class FromCSV(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        with open(settings.MEDIA_ROOT / filename, "r") as file_in:
            reader = csv.reader(file_in, delimiter=",")
            contents = [line for line in reader]
        delete_file_on_server(filename)

        if data := contents[1:]:  # [1] headers is not required
            Sleep.populate_from_csv(data)
            messages.success(request, "Sleep data successfully uploaded.")
            return redirect("aida:sleep-list")
        messages.error(request, "Failed to read data from CSV.")
        return redirect("aida:data-import")


class ToJSON(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return to_json_response("sleep_data", Sleep.all_to_json())


class FromJSON(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        with open(settings.MEDIA_ROOT / filename, "r") as file_in:
            contents = json.load(file_in)
        delete_file_on_server(filename)

        if data := contents.get("data", None):
            try:
                Sleep.populate_from_json(data)
                messages.success(request, "Sleep data successfully imported.")
                return redirect("aida:sleep-list")
            except ValueError:
                messages.error(request, "Failed to decode JSON.")
        else:
            messages.error(request, "Failed to import sleep data.")
        return render(request, "aida/file/import.html")
