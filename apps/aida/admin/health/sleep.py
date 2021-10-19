from django.contrib import admin

from apps.aida.models.health.sleep import Sleep


@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    list_display = ("slept_at", "awoke_at", "duration_")
    readonly_fields = ("duration",)

    def duration_(self, obj):
        return obj.duration_formatted()
