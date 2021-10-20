from django.contrib import admin

from apps.aida.models.health.pulse import HeartRate


@admin.register(HeartRate)
class HeartRateAdmin(admin.ModelAdmin):
    list_display = ("pulse", "condition")

    def condition(self, obj):
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
