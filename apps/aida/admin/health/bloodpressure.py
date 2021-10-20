from django.contrib import admin

from apps.aida.models.health.bloodpressure import BloodPressure


@admin.register(BloodPressure)
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ("systolic", "diastolic")
