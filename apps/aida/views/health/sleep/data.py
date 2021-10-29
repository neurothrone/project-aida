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

from apps.aida.models.health.sleep import Sleep


def csv_response(filename: str, header: list[str], data: dict) -> HttpResponse:
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f"attachment;filename={filename}.csv"}, )
    writer = csv.DictWriter(response, delimiter=",", lineterminator="\n", fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    return response


def json_response(filename: str, data: dict) -> HttpResponse:
    response = HttpResponse(
        json.dumps(data),
        content_type="application/json",
        headers={"Content-Disposition": f"attachment;filename={filename}.json"})
    return response


class ToCSV(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        header, data = Sleep.all_to_csv()
        return csv_response("sleep_data", header, data)


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
        return json_response("sleep_data", Sleep.all_to_json())


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
