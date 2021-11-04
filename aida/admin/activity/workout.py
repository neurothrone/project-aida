from django.contrib import admin

from aida.admin.activity import ActivityMetricAdmin
from aida.admin.activity.inlines import ExerciseInline
from aida.models.activity.workout import Workout


@admin.register(Workout)
class WorkoutAdmin(ActivityMetricAdmin):
    fields = ("type", "engaged_at")
    list_display = ("id", "type", "engaged_at_")
    inlines = (ExerciseInline,)
    list_filter = ("type", "engaged_at")
