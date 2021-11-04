import csv
import json

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def delete_file_on_server(filename: str) -> None:
    fs = FileSystemStorage()
    uploaded_file_path = fs.path(filename)
    fs.delete(uploaded_file_path)


def to_csv_response(filename: str, header: list[str], data: dict) -> HttpResponse:
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f"attachment;filename={filename}.csv"}, )
    writer = csv.DictWriter(response, delimiter=",", lineterminator="\n", fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    return response


def to_json_response(filename: str, data: dict) -> HttpResponse:
    return HttpResponse(json.dumps(data),
                        content_type="application/json",
                        headers={"Content-Disposition": f"attachment;filename={filename}.json"})


def get_data_from_csv(filename: str) -> list:
    with open(settings.MEDIA_ROOT / filename, "r") as file_in:
        reader = csv.reader(file_in, delimiter=",")
        contents = [line for line in reader]
    delete_file_on_server(filename)
    return contents


def get_data_from_json(filename: str) -> dict:
    with open(settings.MEDIA_ROOT / filename, "r") as file_in:
        contents = json.load(file_in)
    delete_file_on_server(filename)
    return contents
