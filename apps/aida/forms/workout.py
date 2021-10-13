from django import forms

from apps.aida.models.activity.workout.base import Workout


class WorkoutForm(forms.ModelForm):
    trained_at = forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"],
                                     widget=forms.DateTimeInput(format="%d/%m/%Y %H:%M"))

    class Meta:
        model = Workout
        fields = ("type", "trained_at")
        labels = {
            "type": "Workout Type",
        }

    def __init__(self, *args, **kwargs) -> None:
        super(WorkoutForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
