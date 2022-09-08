from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserForm(AuthenticationForm):
    username =  forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'myfieldclass'}))
    

# class UserForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=50 ,widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'myfieldclass'}))