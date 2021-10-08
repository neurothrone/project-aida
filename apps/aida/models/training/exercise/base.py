from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    vest_weight = models.PositiveSmallIntegerField(default=0)
