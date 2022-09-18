from django import forms

class task_form(forms.Form):
    content = forms.CharField(max_length=50, label='')