from collections import namedtuple

from django.test import TestCase
from django.urls import reverse

from apps.aida.models.health.sleep import Sleep

SleepData = namedtuple("SleepData", "slept_at awoke_at")
SleepField = namedtuple("SleepField", "attribute expected_label")

SLEEP_DATA = [
    SleepData(slept_at="2021-10-25 02:30:00+00:00", awoke_at="2021-10-25 12:00:00+00:00"),
    SleepData(slept_at="2021-10-26 08:00:00+00:00", awoke_at="2021-10-26 16:00:00+00:00"),
    SleepData(slept_at="2021-10-27 08:00:00+00:00", awoke_at="2021-10-27 16:50:00+00:00")
]
TEST_SLEEP_FIELDS = [
    SleepField("slept_at", "slept at"),
    SleepField("awoke_at", "awoke at"),
    SleepField("duration", "duration"),
]


class SleepModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for data in SLEEP_DATA:
            Sleep.create(slept_at=data.slept_at, awoke_at=data.awoke_at)

    def test_field_labels(self):
        """Tests if all the resulting labels are equal to the expected labels."""
        sleep = Sleep.find_by_id(1)
        for test_obj in TEST_SLEEP_FIELDS:
            result = sleep._meta.get_field(test_obj.attribute).verbose_name
            self.assertEqual(result, test_obj.expected_label)

    def test_get_absolute_url(self):
        """Tests if the get_absolute_url() for a Sleep object is equal to the one in urlconf."""
        sleep = Sleep.find_by_id(1)
        self.assertEqual(sleep.get_absolute_url(),
                         reverse("aida:sleep-detail", kwargs={"pk": sleep.id}))
