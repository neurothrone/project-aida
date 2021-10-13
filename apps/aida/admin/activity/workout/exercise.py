from django.contrib import admin
from django.utils.html import format_html

from apps.aida.admin.activity.workout.inlines import CardioSetInline
from apps.aida.admin.activity.workout.inlines import WeightSetInline
from apps.aida.models.activity.workout.exercise import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "vest_weight", "total")
    inlines = (CardioSetInline, WeightSetInline)
    search_fields = ("name",)

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
