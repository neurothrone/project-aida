from django.test import TestCase

from apps.aida.models.activity.exercise import Exercise
from apps.aida.models.activity.workout import Workout
from apps.aida.tests.activity.workout import data
from apps.aida.tests.util import get_field_max_length
from apps.aida.tests.util import get_field_verbose_name


class ExerciseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        workout = Workout.create("weight", "2021-10-25 02:30:00+00:00")
        for datum in data.EXERCISE_DATA:
            Exercise.create(workout, datum.type, datum.name, datum.vest_weight)

    def test_field_labels(self):
        """Tests if all the resulting labels are equal to the expected labels."""
        exercise = Exercise.find_by_id(1)
        for test in data.EXERCISE_FIELDS:
            result = get_field_verbose_name(exercise, test.attribute)
            self.assertEqual(result, test.expected_label)

    def test_field_max_length(self):
        """Tests if the max length of a label is equal to the expected label."""
        exercise = Exercise.find_by_id(1)
        for test in data.EXERCISE_MAX_LENGTHS:
            result = get_field_max_length(exercise, test.attribute)
            self.assertEqual(result, test.max_length)
