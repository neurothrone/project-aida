from dataclasses import dataclass

from django.test import TestCase

from apps.aida.models.activity.exercise import Exercise
from apps.aida.models.activity.workout import Workout


@dataclass
class ExerciseData:
    type: str
    name: str
    vest_weight: float


@dataclass
class ExerciseFieldTest:
    attribute: str
    expected_label: str


@dataclass
class ExerciseFieldMaxLengthTest:
    attribute: str
    max_length: int


EXERCISE_DATA = [
    ExerciseData("c", "Row", 0),
    ExerciseData("w", "Bench press", 0),
    ExerciseData("w", "Overhead pass", 0)
]
EXERCISE_FIELDS = [
    ExerciseFieldTest(attribute="workout", expected_label="workout"),
    ExerciseFieldTest(attribute="type", expected_label="type"),
    ExerciseFieldTest(attribute="name", expected_label="name"),
    ExerciseFieldTest(attribute="vest_weight", expected_label="vest weight")
]
EXERCISE_MAX_LENGTHS = [
    ExerciseFieldMaxLengthTest(attribute="type", max_length=25),
    ExerciseFieldMaxLengthTest(attribute="name", max_length=255)
]


class ExerciseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        workout = Workout.create("weight", "2021-10-25 02:30:00+00:00")
        for data in EXERCISE_DATA:
            Exercise.create(workout, data.type, data.name, data.vest_weight)

    def test_field_labels(self):
        """Tests if all the resulting labels are equal to the expected labels."""
        exercise = Exercise.find_by_id(1)
        for test_obj in EXERCISE_FIELDS:
            result = exercise._meta.get_field(test_obj.attribute).verbose_name
            self.assertEqual(result, test_obj.expected_label)

    def test_field_max_length(self):
        """Tests if the max length of a label is equal to the expected label."""
        exercise = Exercise.find_by_id(1)
        for test in EXERCISE_MAX_LENGTHS:
            result = exercise._meta.get_field(test.attribute).max_length
            self.assertEqual(result, test.max_length)
