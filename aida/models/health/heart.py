from datetime import datetime

from django.conf import settings
from django.db import models

from aida.models.health import Health
from shared.utils import dt


class Heart(Health):
    measured_at = models.DateTimeField(help_text="Enter the date and time the measurement took place")
    systolic = models.PositiveSmallIntegerField(help_text="Enter the systolic value (the upper value)")
    diastolic = models.PositiveSmallIntegerField(help_text="Enter diastolic value (the lower value)")
    pulse = models.PositiveSmallIntegerField(help_text="Enter your hearts beats per minute")

    class Meta:
        verbose_name_plural = "Heart metrics"
        ordering = ["-measured_at"]

    def __str__(self) -> str:
        return f"{self.measured_at.date()} | {self.systolic} / {self.diastolic} | {self.pulse}"

    def measured_at_table_format(self) -> str:
        return self.datetime_table_format(self.measured_at)

    # region DataConvertableMixin

    @staticmethod
    def create(measured_at: str, systolic: int, diastolic: int, pulse: int) -> "Heart":
        return Heart.objects.create(measured_at=dt.parse_datetime(measured_at),
                                    systolic=systolic,
                                    diastolic=diastolic,
                                    pulse=pulse)

    @staticmethod
    def db_data_to_csv():
        header = ["measured_at", "systolic", "diastolic", "pulse"]
        return header, Heart.db_data_to_json()["data"]

    @staticmethod
    def db_data_to_json():
        hearts: list[Heart] = Heart.find_all()
        content = {
            "category": "sleep",
            "timezone": settings.TIME_ZONE,
            "data": [],
        }
        for heart in hearts:
            content["data"].append({
                "measured_at": str(heart.measured_at),
                "systolic": heart.systolic,
                "diastolic": heart.diastolic,
                "pulse": heart.pulse
            })
        return content

    # endregion DataConvertableMixin

    # region ViewUrlsMixin

    @property
    def detail_url(self) -> str:
        return "aida:heart-detail"

    @property
    def update_url(self) -> str:
        return "aida:heart-update"

    @property
    def delete_url(self) -> str:
        return "aida:heart-delete"

    # endregion ViewUrlsMixin

    @classmethod
    def all_to_chart_data(cls) -> dict:
        queryset = cls.objects.all().order_by("measured_at")

        dates = [heart.date_table_format(heart.measured_at) for heart in queryset]
        pulses = [heart.pulse for heart in queryset]

        return {
            "labels": dates,
            "chart_data": pulses,
            "chart_label": "Pulse vs Date"
        }
