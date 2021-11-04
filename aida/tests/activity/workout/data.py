from dataclasses import dataclass


@dataclass
class WorkoutData:
    type: str
    engaged_at: str


@dataclass
class WorkoutFieldTest:
    attribute: str
    expected_label: str


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


WORKOUT_DATA = [
    WorkoutData("cardio", "2021-09-20 20:00:00+00:00"),
    WorkoutData("weight", "2021-09-21 03:00:00+00:00")
]
WORKOUT_FIELDS = [
    WorkoutFieldTest("engaged_at", "engaged at"),
    WorkoutFieldTest("type", "type")
]

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
