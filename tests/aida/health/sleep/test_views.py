from django.test import TestCase

from rest_framework import status


class ViewsTestCase(TestCase):
    def test_sleep_list_loads_properly(self):
        """Tests if the Sleep list view loads properly."""
        response = self.client.get("http://127.0.0.1:8000/aida/health/sleep/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
