from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import task_form
from .models import task_model
from django.contrib.auth.models import User

# Create your views here.

def create_task(request):
    form = task_form()
    if request.method == 'POST':
        form = task_form(request.POST)
        if form.is_valid():
            task = task_model(content=form.cleaned_data['content'], creator=request.user.username)
            task.save()
            return redirect('/')
    context = {
        'form': form,
    }

    return render(request, 'tasks/create_task.html', context=context)