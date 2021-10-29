import csv

from django.contrib import messages
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

        data = Sleep.find_all()
        headers = ["slept_at", "awoke_at"]
        writer = csv.writer(response)
        writer.writerow(headers)
        for sleep in data:
            # output: (tz: utc)
            # need to implement import csv
            # 2021-10-27 08:00:00+00:00,2021-10-27 16:50:00+00:00
            writer.writerow([sleep.slept_at, sleep.awoke_at])
        return response


class FromCSV(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        pass


class ToJSON(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        url = rf_reverse("api:health-sleep-list", request=request)
        r = requests.get(url, params=request.GET)
        if r.status_code == status.HTTP_200_OK:
            data = r.content.decode("utf-8")
            response = HttpResponse(
                data,
                content_type="application/json",
                headers={"Content-Disposition": "attachment;filename=sleep_data.json"})
            return response
        messages.error(request, "Failed to save data to JSON.")
        return render(request, "aida/health/sleep/list.html")
