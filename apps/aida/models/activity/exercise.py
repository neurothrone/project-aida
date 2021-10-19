from django.db import models

from apps.aida.models.activity.workout import Workout
from shared.models.base import BaseModel

EXERCISE_TYPES = [
    ("c", "Cardio"),
    ("w", "Weight"),
    ("u", "Undefined"),
]


class Exercise(BaseModel):
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
