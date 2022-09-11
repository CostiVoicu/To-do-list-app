from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserForm(AuthenticationForm):
    username =  forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class': 'myfieldclass', 'placeholder':'Username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'myfieldclass', 'placeholder':'Password'}), label='')