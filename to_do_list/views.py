from django.shortcuts import render
from tasks.models import Task

def home_view(request):
    tasks_list = Task.objects.all()

    context = {
        'tasks': tasks_list,
    }

    return render(request, "home.html", context=context)