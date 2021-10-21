from rest_framework import serializers

from apps.aida.models.health.sleep import Sleep


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ("slept_at", "awoke_at")
