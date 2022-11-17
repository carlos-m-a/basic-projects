from django import forms
from . import models

class MyForm(forms.ModelForm):
    class Meta:
        model = models.MyModel
        fields = ['name', 'small_int', 'type', 'boolean_field', 'date']
        labels = {'name':'Name', 'small_int':'Small int', 'type':'Type', 'boolean_field':'Boolean field', 'date':'Date'}
        widgets = {
            'name':forms.TextInput(attrs={"autofocus":True,"class":"form-control", 'placeholder':'Name'}), 
            'small_int':forms.NumberInput(attrs={"class":"form-control", 'placeholder':'Integer'}), 
            'type':forms.Select(attrs={"class":"form-control"}), 
            'boolean_field':forms.CheckboxInput(attrs={}), 
            'date':forms.DateInput(attrs={"autocomplete": "date", "type":"date", "class":"form-control", 'placeholder':'Date'})
            }