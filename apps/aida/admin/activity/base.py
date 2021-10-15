from django.contrib import admin

from apps.aida.admin.activity.inlines import ExerciseInline
from apps.aida.models.activity.workout import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    fields = ("type", "engaged_at")
    list_display = ("type", "engaged_at")
    inlines = (ExerciseInline,)
    list_filter = ("type", "engaged_at")
