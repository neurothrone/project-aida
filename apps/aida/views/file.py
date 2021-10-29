from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View


class Import(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/data/import.html")

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        file = request.FILES.get("data_file", None)
        if not file:
            messages.error(request, "Error! Something went wrong when uploading file.")
            return render(request, "aida/data/import.html")

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        # uploaded_file_path = fs.path(filename)

        if filename.lower().endswith(".csv"):
            return redirect("aida:sleep-from-csv", filename=filename)

        if filename.lower().endswith(".json"):
            return redirect("aida:sleep-from-json", filename=filename)

        messages.error(request, "Error! File type not supported.")
        return render(request, "aida/data/import.html")
