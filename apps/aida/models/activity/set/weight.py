from django.db import models

from apps.aida.models.activity.set import Set

WEIGHT_UNITS = [
    ("g", "Grams"),
    ("k", "Kilograms"),
    ("l", "Pounds"),
]


class WeightSet(Set):
    reps = models.PositiveSmallIntegerField(default=0,
                                            help_text="Enter the amount of repetitions performed in the set")
    weight = models.PositiveSmallIntegerField(default=0,
                                              help_text="Enter the weight the set was performed with")
    weight_unit = models.CharField(choices=WEIGHT_UNITS, default="k",
                                   max_length=10, blank=True, null=True,
                                   help_text="Enter the weight unit of the set")

    def __str__(self) -> str:
        return f"Weight Set of {super().__str__()}"

    @property
    def detail_url(self) -> str:
        return "aida:weight-set-detail"

    @property
    def update_url(self) -> str:
        return "aida:weight-set-update"

    @property
    def delete_url(self) -> str:
        return "aida:weight-set-delete"
