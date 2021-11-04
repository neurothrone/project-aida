import json
import os.path

from django.conf import settings
from django.test import TestCase

from rest_framework import status

from aida.models.health.sleep import Sleep


class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        path_to_file = settings.BASE_DIR / "data/bulk/health/sleep/sleep_data.json"
        if os.path.exists(path_to_file):
            with open(path_to_file, "r") as file_in:
                contents = json.load(file_in)
            Sleep.populate_from_json(contents["data"])

    def test_sleep_list_view_get_request(self):
        response = self.client.get("http://127.0.0.1:8000/aida/health/sleep/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sleep_create_view_get_request(self):
        response = self.client.get("http://127.0.0.1:8000/aida/health/sleep/create/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sleep_create_view_post_request_redirects_successfully(self):
        response = self.client.post("http://127.0.0.1:8000/aida/health/sleep/create/",
                                    {"slept_at": "2021-10-27 08:00:00+00:00",
                                     "awoke_at": "2021-10-27 16:50:00+00:00"})
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_sleep_detail_view_get_request(self):
        response = self.client.get("http://127.0.0.1:8000/aida/health/sleep/detail/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sleep_detail_view_get_request_object_not_found(self):
        response = self.client.get("http://127.0.0.1:8000/aida/health/sleep/detail/-1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sleep_update_view_get_request(self):
        response = self.client.get("http://127.0.0.1:8000/aida/health/sleep/update/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sleep_update_view_object_updates_successfully(self):
        old_object, new_object = Sleep.find_by_id(1), Sleep.find_by_id(2)
        self.client.post("http://127.0.0.1:8000/aida/health/sleep/update/1/",
                         {"slept_at": new_object.slept_at, "awoke_at": new_object.awoke_at})
        self.assertNotEqual(old_object.slept_at, new_object.slept_at)

    def test_sleep_delete_view_get_request(self):
        response = self.client.get("http://127.0.0.1:8000/aida/health/sleep/delete/5/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sleep_delete_view_object_deletes_successfully(self):
        self.client.post("http://127.0.0.1:8000/aida/health/sleep/delete/6/")
        sleep = Sleep.find_by_id(6)
        self.assertEqual(sleep, None)
