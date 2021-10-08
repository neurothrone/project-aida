from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views import View


class IndexView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/index.html")


class ListView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/list.html")


class DetailView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/detail.html")


class CreateView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "aida/create.html")

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        pass
