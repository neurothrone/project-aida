from django.contrib import admin

from apps.aida.models.activity.exercise import Exercise
from apps.aida.models.activity.set.cardio import CardioSet
from apps.aida.models.activity.set.weight import WeightSet


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
