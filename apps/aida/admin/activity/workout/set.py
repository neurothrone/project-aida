from django.contrib import admin

from apps.aida.models.activity.workout.set.cardio import CardioSet
from apps.aida.models.activity.workout.set.weight import WeightSet


@admin.register(CardioSet)
class CardioSetAdmin(admin.ModelAdmin):
    list_display = ("exercise", "speed", "duration", "time_unit")

    def exercise(self, obj):
        return obj.exercise.name


@admin.register(WeightSet)
class WeightSetAdmin(admin.ModelAdmin):
    list_display = ("exercise", "reps", "weight", "weight_unit")

    def exercise(self, obj):
        return obj.exercise.name
