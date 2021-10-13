from django.contrib import admin

from apps.aida.models.health.sleep import Sleep


@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    list_display = ("awake_at", "slept_at", "duration", "duration_hours")
    readonly_fields = ("duration",)

    def duration_hours(self, obj):
        return f"{obj.duration / 60 / 60:.1f} h"

