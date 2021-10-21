from pathlib import Path

from django import forms


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = BASE_DIR / "data/bulk/"


class LoadDataForm(forms.Form):
    file = forms.FileField()


class LoadLocalDataForm(forms.Form):
    file = forms.FilePathField(path=DATA_DIR)
