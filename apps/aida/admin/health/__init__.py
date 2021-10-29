from django.contrib import admin

from apps.aida.models.health import HealthMetric


class HeartMetricAdmin(admin.ModelAdmin):
    def measured_at_(self, obj: HealthMetric) -> str:
        return obj.datetime_table_format(obj.measured_at)
