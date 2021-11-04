from django.test import TestCase
from django.urls import reverse

from aida.models.health.sleep import Sleep
from aida.tests.health.sleep import data
from shared.models.field import get_field_verbose_name


class SleepModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for datum in data.SLEEP_DATA:
            Sleep.create(slept_at=datum.slept_at, awoke_at=datum.awoke_at)

    def test_field_labels(self):
        """Tests if all the resulting labels are equal to the expected labels."""
        sleep = Sleep.find_by_id(1)
        for test in data.TEST_SLEEP_FIELDS:
            result = get_field_verbose_name(sleep, test.attribute)
            # result = sleep._meta.get_field(test.attribute).verbose_name
            self.assertEqual(result, test.expected_label)

    def test_get_absolute_url(self):
        """Tests if the get_absolute_url() for a Sleep object is equal to the one in urlconf."""
        sleep = Sleep.find_by_id(1)
        self.assertEqual(sleep.get_absolute_url(),
                         reverse("aida:sleep-detail", kwargs={"pk": sleep.id}))
