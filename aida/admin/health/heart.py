from django.contrib import admin

from aida.models.health.heart import Heart


@admin.register(Heart)
class HeartAdmin(admin.ModelAdmin):
    list_display = ("id", "measured_at_", "systolic", "diastolic", "pulse", "condition")

    def measured_at_(self, obj: Heart) -> str:
        return obj.datetime_table_format(obj.measured_at)

    def condition(self, obj: Heart) -> str:
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
