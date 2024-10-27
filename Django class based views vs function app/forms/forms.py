from django import forms
from .models import InputFromsModel

class InputForm(forms.ModelForm):
    class Meta:
        model = InputFromsModel
        fields = "__all__"
