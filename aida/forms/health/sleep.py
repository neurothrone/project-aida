from django import forms
from django.core.exceptions import ValidationError

from aida.models.health.sleep import Sleep


class SleepForm(forms.ModelForm):
    class Meta:
        model = Sleep
        fields = ("slept_at", "awoke_at")

    def __init__(self, *args, **kwargs) -> None:
        super(SleepForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

    def clean(self):
        data = self.cleaned_data
        slept_at = self.cleaned_data["slept_at"]
        awoke_at = self.cleaned_data["awoke_at"]

        if slept_at >= awoke_at:
            raise ValidationError("Invalid slept_at date.")

        if awoke_at <= slept_at:
            raise ValidationError("Invalid awoke_at date.")

        return data
