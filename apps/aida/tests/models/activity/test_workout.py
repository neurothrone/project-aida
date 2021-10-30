from dataclasses import dataclass

from django.test import TestCase

from apps.aida.models.activity.workout import Workout


@dataclass
class WorkoutData:
    type: str
    engaged_at: str


@dataclass
class WorkoutFieldTest:
    attribute: str
    expected_label: str


WORKOUT_DATA = [
    WorkoutData("cardio", "2021-09-20 20:00:00+00:00"),
    WorkoutData("weight", "2021-09-21 03:00:00+00:00")
]
WORKOUT_FIELDS = [
    WorkoutFieldTest("engaged_at", "engaged at"),
    WorkoutFieldTest("type", "type")
]


class WorkoutModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        for data in WORKOUT_DATA:
            Workout.create(workout_type=data.type, engaged_at=data.engaged_at)

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
        for test_obj in WORKOUT_FIELDS:
            result = exercise._meta.get_field(test_obj.attribute).verbose_name
            self.assertEqual(result, test_obj.expected_label)

    def test_type_field_max_length(self) -> None:
        workout = Workout.find_by_id(1)
        result = workout._meta.get_field("type").max_length
        self.assertEqual(result, 255)
