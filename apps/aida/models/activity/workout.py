from datetime import datetime

from django.db import models
from django.utils.timezone import make_aware

from apps.aida.models.activity.base import Activity

WORKOUT_TYPES = [
    ("cardio", "Cardio Workout"),
    ("weight", "Weight Workout"),
]


class Workout(Activity):
    type = models.CharField(choices=WORKOUT_TYPES, max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.type.title()} | {self.engaged_at.date()}"

    class Meta:
        ordering = ("-engaged_at",)

    @staticmethod
    def create(workout_type: str, engaged_at: str) -> "Workout":
        """Creates a workout object, stores it in the database and returns the object.

        Args:
            workout_type (str): type of workout, can be <cardio> or <weight>.
            engaged_at (str): str to format into datetime object with format YYYY-MM-DD HH:MM.

        Returns:
            Workout: the workout object that was created.
        """

        aware_dt = make_aware(datetime.strptime(engaged_at, "%Y-%m-%d %H:%M"))
        return Workout.objects.create(type=workout_type, engaged_at=aware_dt)

