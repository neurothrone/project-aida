from django.contrib import admin

from apps.aida.admin.health import HeartMetricAdmin
from apps.aida.models.health.bloodpressure import BloodPressure


@admin.register(BloodPressure)
class BloodPressureAdmin(HeartMetricAdmin):
    list_display = ("id", "measured_at_", "systolic", "diastolic", "condition")

    def condition(self, obj: BloodPressure) -> str:
        return "Good?"
