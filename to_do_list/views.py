from django.shortcuts import render
from tasks.models import task_model
from tasks.models import task_model

def home_view(request):
    tasks_list = task_model.objects.all()

    context = {
        'tasks': tasks_list,
    }

    return render(request, "home.html", context=context)