from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from aida.forms.file import FileForm


class Import(View):
    REDIRECT_URLS = {
        "heart": {
            "csv": "aida:heart-from-csv",
            "json": "aida:heart-from-json",
        },
        "sleep": {
            "csv": "aida:sleep-from-csv",
            "json": "aida:sleep-from-json"
        }
    }

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/file/import.html", {"form": FileForm()})

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            category, extension = request.POST["category"], request.POST["extension"]

            if not filename.lower().endswith(f".{extension}"):
                messages.error(request, "Error! Selected extension does not match file extension.")
                return render(request, "aida/file/import.html", {"form": FileForm()})

            if url := Import.REDIRECT_URLS.get(category, {}).get(extension):
                return redirect(url, filename)

        messages.error(request, "Error! Category or file type not supported.")
        return render(request, "aida/file/import.html", {"form": FileForm()})
