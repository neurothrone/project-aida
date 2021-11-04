from django.contrib import admin

from aida.models.activity.set.cardio import CardioSet
from aida.models.activity.set.weight import WeightSet


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
