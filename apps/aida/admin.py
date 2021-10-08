from django.contrib import admin

from apps.aida.models.training.weight import WeightTraining
from apps.aida.models.training.exercise.weight import WeightExercise
from apps.aida.models.training.exercise.set import Set


class WeightExerciseInline(admin.TabularInline):
    can_delete = True
    model = WeightExercise
    extra = 0


class SetInline(admin.TabularInline):
    can_delete = True
    model = Set
    extra = 0


@admin.register(WeightTraining)
class WeightTrainingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "exercised_on")
    inlines = (WeightExerciseInline,)


@admin.register(WeightExercise)
class WeightExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "weight", "vest_weight")
    inlines = (SetInline,)


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ("name", "reps")

    def name(self, obj):
        return obj.exercise.name
