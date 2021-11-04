from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from aida.models.health.sleep import Sleep
from aida.views.utils import get_data_from_csv
from aida.views.utils import get_data_from_json
from aida.views.utils import to_csv_response
from aida.views.utils import to_json_response


class FromCSV(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        contents = get_data_from_csv(filename)

        if data := contents[1:]:  # skip headers
            Sleep.populate_db_from_csv(data)
            messages.success(request, "Sleep data successfully uploaded.")
            return redirect("aida:sleep-list")

        messages.error(request, "Failed to read data from CSV.")
        return redirect("aida:data-import")


class FromJSON(View):
    @staticmethod
    def get(request: HttpRequest, filename: str) -> HttpResponse:
        contents = get_data_from_json(filename)

        if data := contents.get("data", None):
            try:
                Sleep.populate_db_from_json(data)
                messages.success(request, "Sleep data successfully imported.")
                return redirect("aida:sleep-list")
            except ValueError:
                messages.error(request, "Failed to decode JSON.")
        else:
            messages.error(request, "Failed to import sleep data.")
        return render(request, "aida/file/import.html")


class ToCSV(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return to_csv_response("sleep_data", *Sleep.db_data_to_csv())


class ToJSON(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return to_json_response("sleep_data", Sleep.db_data_to_json())
