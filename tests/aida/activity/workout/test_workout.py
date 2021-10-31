from django.test import TestCase

from apps.aida.models.activity.workout import Workout
from tests.aida.activity.workout import data
from tests.util import get_field_verbose_name


class WorkoutModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        for datum in data.WORKOUT_DATA:
            Workout.create(workout_type=datum.type, engaged_at=datum.engaged_at)

    # TODO: test failure of creation if possible with erroneous arguments
    def test_invalid_arguments(self):
        pass

    def test_find_all(self):
        workouts = Workout.find_all()
        self.assertNotEqual(workouts, None)

    def test_find_by_type(self):
        cardio_workouts = Workout.objects.filter(type="cardio")
        self.assertNotEqual(cardio_workouts, None)

    def test_compare_workouts(self):
        cardio_workout = Workout.objects.filter(type="cardio").first()
        weight_workout = Workout.objects.filter(type="weight").first()
        self.assertNotEqual(cardio_workout.type, weight_workout.type)

    def test_field_labels(self):
        """Tests if all the resulting labels are equal to the expected labels."""
        exercise = Workout.find_by_id(1)
        for test in data.WORKOUT_FIELDS:
            result = get_field_verbose_name(exercise, test.attribute)
            self.assertEqual(result, test.expected_label)

    def test_type_field_max_length(self) -> None:
        workout = Workout.find_by_id(1)
        result = workout._meta.get_field("type").max_length
        self.assertEqual(result, 255)
