from datetime import datetime

from django.db import models
from django.utils.timezone import make_aware

from apps.aida.models.activity import Activity

WORKOUT_TYPES = [
    ("c", "Cardio Workout"),
    ("w", "Weight Workout"),
]


class Workout(Activity):
    type = models.CharField(choices=WORKOUT_TYPES, max_length=255,
                            help_text="Select the type of workout")

    def __str__(self) -> str:
        return f"{self.get_type_display()} | {self.engaged_at.date()}"

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

    @property
    def detail_url(self) -> str:
        return "aida:workout-detail"

    @property
    def update_url(self) -> str:
        return "aida:workout-update"

    @property
    def delete_url(self) -> str:
        return "aida:workout-delete"
