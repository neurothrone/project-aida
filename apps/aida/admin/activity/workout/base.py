from django.contrib import admin

from apps.aida.admin.activity.workout.inlines import ExerciseInline
from apps.aida.models.activity.workout.base import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("type", "trained_at")
    inlines = (ExerciseInline,)
    list_filter = ("type", "trained_at")
