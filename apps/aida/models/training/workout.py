from django.db import models


class Workout(models.Model):
    exercised_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
