from django.db import models

from apps.aida.models.activity.workout import Workout
from shared.models.base import BaseModel
from shared.models.urls import ViewUrlsMixin

EXERCISE_TYPES = [
    ("c", "Cardio"),
    ("w", "Weight"),
    ("u", "Undefined"),
]


class Exercise(BaseModel, ViewUrlsMixin):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE,
                                help_text="The workout the exercise belongs to")
    type = models.CharField(choices=EXERCISE_TYPES, max_length=25,
                            help_text="Select the type of the exercise")
    name = models.CharField(max_length=255,
                            help_text="The name of the exercise")
    vest_weight = models.FloatField(default=0,
                                    help_text="Additional weight with a vest")

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def create(workout: Workout, type: str, name: str, vest_weight: float) -> "Exercise":
        """Creates an Exercise object, stores it in the database and returns the object.

        Args:
            workout (Workout): workout object this exercise belongs to.
            type (str): type of exercise, can be <cardio> or <weight>.
            name (str): the name of the exercise.
            vest_weight (float): additional weight added with a vest.

        Returns:
            Exercise: the Exercise object that was created.
        """

        return Exercise.objects.create(workout=workout,
                                       type=type,
                                       name=name,
                                       vest_weight=vest_weight)

    @property
    def detail_url(self) -> str:
        return "aida:exercise-detail"

    @property
    def update_url(self) -> str:
        return "aida:exercise-update"

    @property
    def delete_url(self) -> str:
        return "aida:exercise-delete"
