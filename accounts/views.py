from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import user_form, register_form

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = user_form(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = user_form(request)
    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context=context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'accounts/logout.html', {})

def register_view(request):
    form = register_form(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)