from django import forms

from apps.aida.models.training.workout import Workout


class WorkoutForm(forms.ModelForm):
    trained = forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"],
                                  widget=forms.DateTimeInput(format="%d/%m/%Y %H:%M"))

    class Meta:
        model = Workout
        fields = ("type", "trained")
        labels = {
            "type": "Workout Type",
        }

    def __init__(self, *args, **kwargs) -> None:
        super(WorkoutForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

    # def clean(self):
    #     super(WorkoutForm, self).clean()
    #     type_ = self.cleaned_data.get("type")
    #     print(f"Type = {type_}")
    #
    #     try:
    #         dt = self.cleaned_data.get("trained")
    #         print(f"dt = {dt}")
    #         trained = datetime.strptime(dt, "%d/%m/%Y %H:%M")
    #         self.cleaned_data["trained"] = trained
    #     except ValueError:
    #         self._errors["trained"] = self.error_class([
    #             "Trained must be in the format %d/%m/%Y %H:%M"
    #         ])
    #     return self.cleaned_data
