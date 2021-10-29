from django.contrib import admin

from apps.aida.admin.health import HeartMetricAdmin
from apps.aida.models.health.heartrate import HeartRate


@admin.register(HeartRate)
class HeartRateAdmin(HeartMetricAdmin):
    list_display = ("id", "measured_at_", "pulse", "condition")

    def condition(self, obj: HeartRate) -> str:
        if obj.pulse == 0:
            return "Dead"
        elif obj.pulse < 40:
            return "Alarmingly low"
        elif obj.pulse < 60:
            return "Low"
        elif obj.pulse <= 80:
            return "Good"
        elif obj.pulse > 80:
            return "Elevated"
        elif obj.pulse > 140:
            return "Alarmingly elevated"
        return "Undefined"
