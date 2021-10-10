from django.contrib import admin
from django.utils.html import format_html

from apps.aida.models.training.exercise import Exercise
from apps.aida.models.training.workout import Workout
from apps.aida.models.training.set.cardio import CardioSet
from apps.aida.models.training.set.weight import WeightSet


class ExerciseInline(admin.TabularInline):
    can_delete = True
    model = Exercise
    extra = 0


class CardioSetInline(admin.TabularInline):
    can_delete = True
    model = CardioSet
    extra = 0


class WeightSetInline(admin.TabularInline):
    can_delete = True
    model = WeightSet
    extra = 0


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("type", "trained")
    inlines = (ExerciseInline,)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "vest_weight", "total")
    inlines = (CardioSetInline, WeightSetInline)

    def total(self, obj):
        sets = obj.weightset_set.all()
        if sets:
            reps = 0
            for set_ in sets:
                reps += set_.reps
            return format_html("<b>{}</b> reps", reps)
        sets = obj.cardioset_set.all()
        if sets:
            time_unit = sets[0].time_unit
            duration = 0
            for set_ in sets:
                duration += set_.duration
            return format_html("<b>{}</b> {}", duration, time_unit)
        return "Undefined"


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
