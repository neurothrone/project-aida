from django.contrib import admin

from aida.models.health.sleep import Sleep


@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    list_display = ("id", "slept_at_", "awoke_at_", "duration_")
    readonly_fields = ("duration",)

    def duration_(self, obj: Sleep) -> str:
        return obj.duration_formatted()

    def slept_at_(self, obj: Sleep) -> str:
        return obj.datetime_table_format(obj.slept_at)

    def awoke_at_(self, obj: Sleep) -> str:
        return obj.datetime_table_format(obj.awoke_at)
