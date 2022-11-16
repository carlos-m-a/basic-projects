from django import forms
from . import models

class MyForm(forms.ModelForm):
    class Meta:
        model = models.MyModel
        fields = '__all__'