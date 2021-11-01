from django.contrib import admin

from apps.aida.admin.activity.exercise import ExerciseAdmin
from apps.aida.admin.activity.set import CardioSetAdmin
from apps.aida.admin.activity.set import WeightSetAdmin
from apps.aida.admin.activity.workout import WorkoutAdmin
from apps.aida.admin.health.heart import HeartAdmin
from apps.aida.admin.health.sleep import SleepAdmin


class AidaAdminSite(admin.AdminSite):
    """Customize the order of models in aida admin interface."""

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """

        # retrieve the original list
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

        # set custom ordering of the models for each app
        for app in app_list:
            if app["app_label"] == "aida":
                # names have to the verbose_name_plural or verbose_name of the model
                ordering = {
                    "Workouts": 1,
                    "Exercises": 2,
                    "Cardio sets": 3,
                    "Weight sets": 4,
                    "Heart metrics": 5,
                    "Sleep metrics": 6
                }
                app["models"].sort(key=lambda x: ordering[x["name"]])
        return app_list


admin.AdminSite.get_app_list = AidaAdminSite.get_app_list
