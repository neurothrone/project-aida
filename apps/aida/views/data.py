import csv
import json

from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from apps.aida.models.health.sleep import Sleep


class Import(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/data/import.html")

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        file = request.FILES.get("data_file", None)
        if not file:
            return render(request, "aida/data/import.html")

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_path = fs.path(filename)
        # only supported extensions atm
        if filename.lower().endswith(".json"):
            with open(settings.MEDIA_ROOT / filename, "r") as file_in:
                file_contents = json.load(file_in)

            # create an app or view focused mainly on file loading and saving?
            category = file_contents.get("category", None)
            if category and category == "sleep":
                Sleep.create_from_json(file_contents["data"])
                messages.success(request, f"{category.capitalize()} data successfully uploaded.")
                fs.delete(uploaded_file_path)
                return redirect("aida:sleep-list")
        elif filename.lower().endswith(".csv"):
            # TODO: open with csv
            print("CSV file")
        else:
            messages.error(request, "Error! File type not supported.")
        return render(request, "aida/data/import.html")
