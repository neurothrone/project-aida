from django import forms

from apps.aida.models.health.sleep import Sleep


class SleepForm(forms.ModelForm):
    # engaged_at = forms.DateTimeField(input_formats=["%Y-%m-%d %H:%M"],
    #                                  widget=forms.DateTimeInput(format="%Y-%m-%d %H:%M"))

    class Meta:
        model = Sleep
        fields = "__all__"
        # fields = ("type", "engaged_at")
        # labels = {
        #     "type": "Workout Type",
        # }

    def __init__(self, *args, **kwargs) -> None:
        super(SleepForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
