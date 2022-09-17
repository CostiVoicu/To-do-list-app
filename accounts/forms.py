from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm

class user_form(AuthenticationForm):
    username =  forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class': 'field_class', 'placeholder':'Username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field_class', 'placeholder':'Password'}), label='')

class register_form(UserCreationForm):
    username =  forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class': 'field_class'}))