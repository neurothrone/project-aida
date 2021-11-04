from django import forms

CATEGORIES = (
    ("heart", "Heart"),
    ("sleep", "Sleep"),
)

EXTENSIONS = (
    ("csv", "CSV"),
    ("json", "JSON"),
)


class FileForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORIES)
    extension = forms.ChoiceField(choices=EXTENSIONS)
    file = forms.FileField()

    def __init__(self, *args, **kwargs) -> None:
        super(FileForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key == "file":
                field.widget.attrs.update({"class": "form-control"})
            else:
                field.widget.attrs.update({"class": "form-select mb-3"})
