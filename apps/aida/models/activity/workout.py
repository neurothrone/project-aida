from django.db import models

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
        """Creates a Workout object, stores it in the database and returns the object.

        Args:
            workout_type (str): type of workout, can be <cardio> or <weight>.
            engaged_at (str): str to format into datetime object with format YYYY-MM-DD HH:MM:SStz.

        Returns:
            Workout: the Workout object that was created.
        """

        return Workout.objects.create(type=workout_type, engaged_at=engaged_at)

    @property
    def detail_url(self) -> str:
        return "aida:workout-detail"

    @property
    def update_url(self) -> str:
        return "aida:workout-update"

    @property
    def delete_url(self) -> str:
        return "aida:workout-delete"
