from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views import View


class IndexView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/index.html")
