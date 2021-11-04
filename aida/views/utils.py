import csv
import json

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
