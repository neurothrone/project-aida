from django.contrib import admin

from apps.aida.models.activity import Activity


class ActivityMetricAdmin(admin.ModelAdmin):
    def engaged_at_(self, obj: Activity) -> str:
        return obj.datetime_table_format(obj.engaged_at)
