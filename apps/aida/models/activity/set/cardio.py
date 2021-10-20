from django.db import models

from apps.aida.models.activity.set import Set

TIME_UNITS = [
    ("s", "Seconds"),
    ("m", "Minutes"),
    ("h", "Hours"),
]


class CardioSet(Set):
    speed = models.PositiveSmallIntegerField(default=0,
                                             help_text="Enter the speed the set was performed in (km/h)")
    duration = models.PositiveSmallIntegerField(default=0,
                                                help_text="Enter the duration of the set")
    time_unit = models.CharField(choices=TIME_UNITS, default="m",
                                 max_length=10, blank=True, null=True,
                                 help_text="Enter the time unit of the set")

    def __str__(self) -> str:
        return f"Cardio Set of {super().__str__()}"

    @property
    def detail_url(self) -> str:
        return "aida:cardio-set-detail"

    @property
    def update_url(self) -> str:
        return "aida:cardio-set-update"

    @property
    def delete_url(self) -> str:
        return "aida:cardio-set-delete"
