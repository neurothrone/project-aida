from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from aida.models.health.heart import Heart
from aida.views.utils import get_data_from_csv
from aida.views.utils import get_data_from_json
from aida.views.utils import to_csv_response
from aida.views.utils import to_json_response


class FromCSV(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        contents = get_data_from_csv(filename)
        if data := contents[1:]:  # skip headers
            try:
                Heart.populate_db_from_csv(data)
                messages.success(request, "Heart data successfully uploaded.")
                return redirect("aida:heart-list")
            except TypeError:
                messages.error(request, "Error! Incorrect format in data file for Heart data.")
        else:
            messages.error(request, "Failed to read data from CSV.")
        return redirect("aida:data-import")


class FromJSON(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        contents = get_data_from_json(filename)
        if data := contents.get("data", None):
            try:
                Heart.populate_db_from_json(data)
                messages.success(request, "Heart data successfully imported.")
                return redirect("aida:heart-list")
            except ValueError:
                messages.error(request, "Failed to decode JSON.")
        else:
            messages.error(request, "Failed to import heart data.")
        return render(request, "aida/file/import.html")


class ToCSV(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return to_csv_response("heart_data", *Heart.db_data_to_csv())


class ToJSON(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return to_json_response("heart_data", Heart.db_data_to_json())
