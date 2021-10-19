from django import forms

from apps.aida.models.activity.exercise import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ("type", "name", "vest_weight")
        labels = {
            "type": "Exercise Type",
        }

    def __init__(self, *args, **kwargs) -> None:
        super(ExerciseForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
