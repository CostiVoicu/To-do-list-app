from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserForm(request)
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
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)


# def login_view(request):
#     context = {}
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             username = form['username'].value()
#             password = form['password'].value()
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 messages.error(request, 'username or password not correct')
#                 return redirect('/login/')
#     else:
#         form = UserForm()
#     context['form'] = form
#     return render(request, 'accounts/login.html', context=context)