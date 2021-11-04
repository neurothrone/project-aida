from rest_framework import serializers

from aida.models.health.heart import Heart


class HeartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heart
        fields = ("measured_at", "systolic", "diastolic", "pulse")
